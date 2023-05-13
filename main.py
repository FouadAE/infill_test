from fastapi import Depends, FastAPI, Request, File, UploadFile, Form
from utils.save_to_pinecone import save_to_pinecone
from utils.to_rawtext import convert_to_rawtext
from utils.qa_function import qa_function
from utils.mapping_firebase import map_csv_to_firebase
from utils.extract_properties import extract_properties
import os



app = FastAPI(
    title="FastAPI",
    description="",
    version="0.0.1",
)

# Api root or home endpoint
@app.get('/')
def read_home():
    """
     Home endpoint which can be used to test the availability of the application.
     """
    return {'message': 'System is healthy'}

@app.get("/ping")
def pong():
    return {"ping": "pong!"}


@app.post("/convert")
async def to_raw_text(file: UploadFile = File(...)):
    extension = os.path.splitext(file.filename)[1]
    if (extension == '.csv'):
        file_contents = await file.read()
    elif (extension == '.pdf'):
        file_contents = file.file
    return convert_to_rawtext(extension, file_contents)

@app.post("/save")
async def save(rawtext: str = Form(...), teamid: str = Form(None)):

    return save_to_pinecone(rawtext, teamid)


@app.post('/query')
async def query(query: str = Form(...), teamid: str = Form(None)):
    return qa_function(query, teamid)


@app.post("/mapping")
async def mapping(rawtext:str=Form(...), firebase_schema: str = Form(...)):
    return map_csv_to_firebase(rawtext, firebase_schema)

@app.post("/properties")
async def properties(text:str=Form(...)):
    return extract_properties(text)