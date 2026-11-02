from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch
from pymongo import MongoClient
from dotenv import load_dotenv
from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse 
from typing import TypedDict, Literal
from langchain_community.document_loaders import PyPDFLoader, CSVLoader
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3
import os
import time
import json

load_dotenv()
API = os.getenv("API")
app = FastAPI()
model = ChatGoogleGenerativeAI(model = "gemini-3.5-flash-lite")
embedding = GoogleGenerativeAIEmbeddings(model = "gemini-embedding-001")
client = MongoClient(API)
database  = client['Diesease-Detecion']
collection  = database['evidences']
db = MongoDBAtlasVectorSearch(
    embedding = embedding,
    collection = collection,
    index_name = "vector_index"
)




evidences = [



"""
 "E_151": {
    "name": "E_151",
    "code_question": "E_151",
    "question_fr": "Avez-vous de l’enflure à un ou plusieurs endroits sur votre corps?",
    "question_en": "Do you have swelling in one or more areas of your body?",
    "is_antecedent": false,
    "default_value": 0,
    "value_meaning": {

    },
    "possible-values": [],
""",
"""
 "E_45": {
    "name": "E_45",
    "code_question": "E_45",
    "question_fr": "Avez-vous visualisé du sang dans vos crachats?",
    "question_en": "Have you been coughing up blood?",
    "is_antecedent": false,
    "default_value": 0,
    "value_meaning": {

    },
    "possible-values": [],
""",
"""
"E_194": {
    "name": "E_194",
    "code_question": "E_194",
    "question_fr": "Avez-vous noté un bruit respiratoire aigu surtout à l’inspiration?",
    "question_en": "Have you noticed a high pitched sound when breathing in?",
    "is_antecedent": false,
    "default_value": 0,
    "value_meaning": {

    },
    "possible-values": [],
""",
"""
  "E_83": {
    "name": "E_83",
    "code_question": "E_83",
    "question_fr": "Avez-vous noté une faiblesse au niveau des muscles du visage et/ou des yeux?",
    "question_en": "Have you noticed weakness in your facial muscles and/or eyes?",
    "is_antecedent": false,
    "default_value": 0,
    "value_meaning": {

    },
    "possible-values": [],
""",
"""
 "E_157": {
    "name": "E_157",
    "code_question": "E_157",
    "question_fr": "Avez-vous présentement ou avez-vous eu récemment des engourdissements, une perte de sensibilité ou des fourmillements, dans les mains, les pieds et autour de la bouche?",
    "question_en": "Have you recently had numbness, loss of sensation or tingling, in both arms and legs and around your mouth?",
    "is_antecedent": false,
    "default_value": 0,
    "value_meaning": {

    },
    "possible-values": [],
""",
"""
"E_176": {
    "name": "E_176",
    "code_question": "E_176",
    "question_fr": "Avez-vous noté une faiblesse ou paralysie d’un ou plusieurs de vos membres ou au niveau du visage, encore présentes ou résolues?",
    "question_en": "Did you previously, or do you currently, have any weakness/paralysis in one or more of your limbs or in your face?",
    "is_antecedent": false,
    "default_value": 0,
    "value_meaning": {

    },
    "possible-values": [],
    "data_type": "B"
""",
"""
 "E_42": {
    "name": "E_42",
    "code_question": "E_42",
    "question_fr": "Avez-vous été en contact ou mangé une chose à laquelle vous avez une allergie?",
    "question_en": "Have you been in contact with or ate something that you have an allergy to?",
    "is_antecedent": false,
    "default_value": 0,
    "value_meaning": {

    },
    "possible-values": [],
""",
"""
"E_214": {
    "name": "E_214",
    "code_question": "E_214",
    "question_fr": "Avez-vous noté un un son aigu lorsque vous sortez l’air de vos poumons?",
    "question_en": "Have you noticed a wheezing sound when you exhale?",
    "is_antecedent": false,
    "default_value": 0,
    "value_meaning": {

    },
    "possible-values": [],
""",
"""
"E_150": {
    "name": "E_150",
    "code_question": "E_150",
    "question_fr": "Passez-vous des selles ou des gaz depuis que vos symptômes sont pires?",
    "question_en": "Have you been able to pass stools or gas since your symptoms increased?",
    "is_antecedent": false,
    "default_value": 0,
    "value_meaning": {

    },
    "possible-values": [],
""",
"""
 "E_32": {
    "name": "E_32",
    "code_question": "E_32",
    "question_fr": "Avez-vous une diminution de l’appétit ou des boires?",
    "question_en": "Do you have a decrease in appetite?",
    "is_antecedent": false,
    "default_value": 0,
    "value_meaning": {

    },
    "possible-values": [],
""",
"""
 "E_221": {
    "name": "E_221",
    "code_question": "E_221",
    "question_fr": "Les symptômes ou la douleur sont-ils augmentés avec la toux, un effort comme lever un poids ou quand vous forcez pour aller à la selle?",
    "question_en": "Are the symptoms or pain increased with coughing, with an effort like lifting a weight or from forcing a bowel movement?",
    "is_antecedent": false,
    "default_value": 0,
    "value_meaning": {

    },
    "possible-values": [],
""",
"""
 "E_202": {
    "name": "E_202",
    "code_question": "E_202",
    "question_fr": "Avez-vous une toux aboyante?",
    "question_en": "Does the person have a whooping cough?",
    "is_antecedent": false,
    "default_value": 0,
    "value_meaning": {

    },
    "possible-values": [],
""",
"""
  "E_219": {
    "name": "E_219",
    "code_question": "E_219",
    "question_fr": "Ressentez vous davantage vos symptômes la nuit?",
    "question_en": "Are your symptoms more prominent at night?",
    "is_antecedent": false,
    "default_value": 0,
    "value_meaning": {

    },
    "possible-values": [],
""",
"""
"E_196": {
    "name": "E_196",
    "code_question": "E_196",
    "question_fr": "Avez-vous subi une intervention chirurgicale dans le dernier mois?",
    "question_en": "Have you had surgery within the last month?",
    "is_antecedent": true,
    "default_value": 0,
    "value_meaning": {

    },
    "possible-values": [],
""",
"""
  "E_170": {
    "name": "E_170",
    "code_question": "E_170",
    "question_fr": "Avez-vous des démangeaisons importantes au niveau d’un oeil ou des 2 yeux simultanément?",
    "question_en": "Do you have severe itching in one or both eyes?",
    "is_antecedent": false,
    "default_value": 0,
    "value_meaning": {

    },
    "possible-values": [],
    "data_type": "B"
  },
""",

"""
 "E_77": {
    "name": "E_77",
    "code_question": "E_77",
    "question_fr": "Avez-vous une toux produisant des crachats colorés ou plus abondants qu’habituellement?",
    "question_en": "Do you have a cough that produces colored or more abundant sputum than usual?",
    "is_antecedent": false,
    "default_value": 0,
    "value_meaning": {

    },
""",
"""
 "E_13": {
    "name": "E_13",
    "code_question": "E_13",
    "question_fr": "Trouvez-vous que vos symptômes sont pires depuis environ 2 semaines et que de moins en moins d’effort provoquent les symptômes?",
    "question_en": "Do you find that your symptoms have worsened over the last 2 weeks and that progressively less effort is required to cause the symptoms?",
    "is_antecedent": false,
    "default_value": 0,
    "value_meaning": {

    },
    "possible-values": [],
""",

"""
  "E_14": {
    "name": "E_14",
    "code_question": "E_14",
    "question_fr": "Avez-vous des douleurs au thorax même au repos?",
    "question_en": "Do you have chest pain even at rest?",
    "is_antecedent": false,
    "default_value": 0,
    "value_meaning": {

    },
    "possible-values": [],
    "data_type": "B"
  },
""",

"""
 "E_169": {
    "name": "E_169",
    "code_question": "E_169",
    "question_fr": "Avez-vous le nez et/ou le palais qui pique?",
    "question_en": "Is your nose or the back of your throat itchy?",
    "is_antecedent": false,
    "default_value": 0,
    "value_meaning": {

    },
    "possible-values": [],
""",

"""
 "E_177": {
    "name": "E_177",
    "code_question": "E_177",
    "question_fr": "Avez-vous présentement ou avez-vous eu récemment des engourdissements, une perte de sensibilité ou des fourmillements, n’importe où sur votre le corps?",
    "question_en": "Do you currently, or did you ever, have numbness, loss of sensitivity or tingling anywhere on your body?",
    "is_antecedent": false,
    "default_value": 0,
    "value_meaning": {

    },
    "possible-values": [],
""",

"""
 "E_175": {
    "name": "E_175",
    "code_question": "E_175",
    "question_fr": "Avez-vous de la fatigue, un malaise généralisé, un inconfort vague, des douleurs musculaires diffuses ou une atteinte de votre état général en lien avec votre consultation aujourd’hui?",
    "question_en": "Have you noticed any new fatigue, generalized and vague discomfort, diffuse (widespread) muscle aches or a change in your general well-being related to your consultation today?",
    "is_antecedent": false,
    "default_value": 0,
    "value_meaning": {

    },
    "possible-values": [],
""",

"""
 "E_174": {
    "name": "E_174",
    "code_question": "E_174",
    "question_fr": "Avez-vous remarqué une perte de poids involontaire ou une perte d’appétit qui semble en lien avec votre consultation aujourd’hui?",
    "question_en": "Have you been unintentionally losing weight or have you lost your appetite?",
    "is_antecedent": false,
    "default_value": 0,
    "value_meaning": {

    },
    "possible-values": [],
""",

"""
 "E_145": {
    "name": "E_145",
    "code_question": "E_145",
    "question_fr": "Avez-vous des menstruations très abondantes ou très longues?",
    "question_en": "Do you have very abundant or very long menstruation periods?",
    "is_antecedent": false,
    "default_value": 0,
    "value_meaning": {

    },
    "possible-values": [],
""",

"""
 "E_92": {
    "name": "E_92",
    "code_question": "E_92",
    "question_fr": "Est-ce que vos joues sont devenues rouges soudainement?",
    "question_en": "Did your cheeks suddenly turn red?",
    "is_antecedent": false,
    "default_value": 0,
    "value_meaning": {

    },
    "possible-values": [],
""",

"""
"E_192": {
    "name": "E_192",
    "code_question": "E_192",
    "question_fr": "Avez-vous l’impression qu’il y a des muscles spasmés ou endoloris, dans votre cou, qui vous empêchent de tourner votre tête d’un bord ou de l’autre?",
    "question_en": "Do you feel that muscle spasms or soreness in your neck are keeping you from turning your head to one side?",
    "is_antecedent": false,
    "default_value": 0,
    "value_meaning": {

    },
    "possible-values": [],
""",

"""
"E_188": {
    "name": "E_188",
    "code_question": "E_188",
    "question_fr": "Avez-vous les selles pâles et les urines foncées?",
    "question_en": "Do you have pale stools and dark urine?",
    "is_antecedent": false,
    "default_value": 0,
    "value_meaning": {

    },
    "possible-values": [],
""",

"""
  "E_164": {
    "name": "E_164",
    "code_question": "E_164",
    "question_fr": "Sentez-vous que votre cœur bat de façon très irrégulière ou désorganisée?",
    "question_en": "Do you feel your heart is beating very irregularly or in a disorganized pattern?",
    "is_antecedent": false,
    "default_value": 0,
    "value_meaning": {

    },
    "possible-values": [],
    "data_type": "B"
""",


"""
 "E_193": {
    "name": "E_193",
    "code_question": "E_193",
    "question_fr": "Avez-vous des spasmes musculaires très incommodants au niveau du visage, du cou ou de tout autre endroit de votre corps?",
    "question_en": "Do you have annoying muscle spasms in your face, neck or any other part of your body?",
    "is_antecedent": false,
    "default_value": 0,
    "value_meaning": {

    },
    "possible-values": [],

""",






]



db.add_texts(evidences)
print("successfull")