from fastapi import Depends, FastAPI, Request, File, UploadFile, Form
from utils.save_to_pinecone import save_to_pinecone
from utils.to_rawtext import convert_to_rawtext
from utils.qa_function import qa_function
from utils.mapping_firebase import map_csv_to_firebase
import os



app = FastAPI(
    title="FastAPI",
    description="",
    version="0.0.1",
)


@app.get("/ping")
def pong():
    return {"ping": "pong!"}


@app.post("/save")
async def save(rawtext: str = Form(...), teamid: str = Form(...)):

    return save_to_pinecone(rawtext, teamid)


@app.post('/query')
async def query(query: str = Form(...), teamid: str = Form(...)):
    return qa_function(query, teamid)


@app.post("/convert")
async def create_upload_file(file: UploadFile = File(...)):
    extension = os.path.splitext(file.filename)[1]
    if (extension == '.csv'):
        file_contents = await file.read()
    elif (extension == '.pdf'):
        file_contents = file.file
    return convert_to_rawtext(extension, file_contents)


@app.post("/mapping")
async def mapping1(rawtext:str=Form(...), firebase_schema: str = Form(...)):
    return map_csv_to_firebase(rawtext, firebase_schema)
