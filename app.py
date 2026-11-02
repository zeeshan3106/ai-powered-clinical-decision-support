from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langgraph.checkpoint.sqlite import SqliteSaver
from pymongo import MongoClient
from langchain_mongodb import MongoDBAtlasVectorSearch
from fastapi import FastAPI,Body
from fastapi.responses import StreamingResponse, JSONResponse
from dotenv import load_dotenv
from typing import TypedDict, Literal
import json
import os
import sqlite3
load_dotenv()
app = FastAPI()
model = ChatGoogleGenerativeAI(model = "gemini-3.5-flash-lite")
embedding = GoogleGenerativeAIEmbeddings(model = "gemini-embedding-001")
API = os.getenv('API')
client = MongoClient(API)
database = client['Diesease-Detecion']
collection = database['Records']
data = collection.find({})
db = MongoDBAtlasVectorSearch(
    embedding =embedding,
    collection = collection,
    index_name = "vector_index"
)


collection2 = database['evidences']
db2 = MongoDBAtlasVectorSearch(
    embedding =embedding,
    collection = collection2,
    index_name = "vector_index"
)


class Symptoms(TypedDict):
    symt:list






class State(TypedDict):
    query:str
    codes:list
    stage2:str
    stage3:str
    stage4:str
    stage5:str
    summary:str
    history:str




def Codes(State:State):

    query = State['query']
    rag = db2.as_retriever(
        search_kwargs={
            'k':10
        }
    )
    
    raged = rag.invoke(query)
    print(raged)
    prompt = f"""
    This is the query regarding the patient{query} Analyze the data from this RAG{raged} 
    and provide the codes based on retrieved results. only codes again only codes
    """
    smodel = model.with_structured_output(Symptoms)
    result = smodel.invoke(prompt)
    print(result['symt'])
    State['codes']=result['symt']

    

    return {
       'codes': result['symt']
    }


def PreviousHistory(State:State):
    codes = State['codes']
    query = State['query']

    rag = db.as_retriever(
        search_kwargs={
            'k':20
        }
    )
    raged = rag.invoke(codes)
    prompt = f"""
     Patient query: {query}

    Relevant evidence codes:
    {codes}

    Retrieved patient records:
    {raged}

    Analyze the retrieved information and provide
    a response based on the available records.
    """
    result = model.invoke(prompt)
    final = result.content[0]['text']
    State['history']=final

    return {
        'history':final
    }




def Stage3(State:State):
    query = State['query']
    rag = db.as_retriever(
        search_kwargs={
            'k':20
        }
    )
    raged = rag.invoke(query)
    prompt = f"""
    This is the query regarding the patient{query} Analyze the data from this RAG{raged} and give response to the query of individual
    """
    result = model.invoke(prompt)
    final = result.content[0]['text']

    return {
        'stage1':final
    }


def Stage4(State:State):
    query = State['query']
    rag = db.as_retriever(
        search_kwargs={
            'k':20
        }
    )
    raged = rag.invoke(query)
    prompt = f"""
    This is the query regarding the patient{query} Analyze the data from this RAG{raged} and give response to the query of individual
    """
    result = model.invoke(prompt)
    final = result.content[0]['text']

    return {
        'stage1':final
    }

def Stage5(State:State):
    query = State['query']
    rag = db.as_retriever(
        search_kwargs={
            'k':20
        }
    )
    raged = rag.invoke(query)
    prompt = f"""
    This is the query regarding the patient{query} Analyze the data from this RAG{raged} and give response to the query of individual
    """
    result = model.invoke(prompt)
    final = result.content[0]['text']

    return {
        'stage1':final
    }

def Summary(State:State):
    query = State['query']
    stage1:State['']
    stage2:State['stage2']
    stage3:State['stage3']
    stage4:State['stage4']
    stage5:State['stage5']


    prompt = f"""
    Thsi is the query and this is the data from 5 stages of RAG, give me the final Analysis,
    stage1:{stage1}
    stage2:{stage2}
    stage3:{stage3}
    stage4:{stage4}
    stage5:{stage5}
    """
    result = model.invoke(prompt)
    final = result.content[0]['text']
    State['summary']= final
    return {
        'summary':final
    }

graph = StateGraph(State)

graph.add_node('codes', Codes)
graph.add_node('history',PreviousHistory)
graph.add_node('stage3', Stage3)
graph.add_node('stage4', Stage4)
graph.add_node('stage5', Stage5)
graph.add_node('summary', Summary)


graph.add_edge(START, 'codes')
graph.add_edge('codes','history')
graph.add_edge('history',END)
# graph.add_edge('stage3','stage4')
# graph.add_edge('stage4','stage5')
# graph.add_edge('stage5', END)
# graph.add_edge('summary', END)

connect = sqlite3.connect(database = "abc.db", check_same_thread=False)
checkpointer = SqliteSaver(connect)
config = {'configurable':{'thread_id':1}}
@app.post('/get')
def ClinicGet(query:str = Body(...)):
    workflow = graph.compile(checkpointer=checkpointer)
    initial_state = {'query':query}
    final = workflow.invoke(initial_state, config = config)
    
    return JSONResponse(status_code=200, content = final['history'])