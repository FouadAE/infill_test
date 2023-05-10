from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone 
import time
import os
from dotenv import load_dotenv

load_dotenv()



  # set your API keys
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
PINECONE_API_KEY = os.environ['PINECONE_API_KEY']
PINECONE_API_ENV = os.environ['PINECONE_API_ENV']

def save_to_pinecone(raw_text,teamid):

    #set your raw text
    data = raw_text 

    start = time.time()
    # split text into chunks
    text_splitter = CharacterTextSplitter(        
       separator = "\n",
        chunk_size = 1000,
        chunk_overlap  = 0,
       length_function = len,
        )
    texts = text_splitter.split_text(data)
    print(texts)

   

    # initialize embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    # initialize pinecone
    pinecone.init(
     api_key=PINECONE_API_KEY,  
     environment=PINECONE_API_ENV  
    )
    index_name = "pinecone-test"
    # set your pinecone index
    Pinecone.from_texts(texts, embeddings, index_name=index_name,namespace=teamid)

    end = time.time()
    print(end - start)
    return "saved to pinecone"
