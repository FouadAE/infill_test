from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone 
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
import time
import os
from dotenv import load_dotenv

load_dotenv()



  # set your API keys
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
PINECONE_API_KEY = os.environ['PINECONE_API_KEY']
PINECONE_API_ENV = os.environ['PINECONE_API_ENV']


def qa_function(query,teamid):
    start = time.time()
    # initialize embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    # initialize pinecone
    pinecone.init(
     api_key=PINECONE_API_KEY,  
     environment=PINECONE_API_ENV  
    )
    index_name = "pinecone-test"

    docsearch = Pinecone.from_texts("", embeddings, index_name=index_name,namespace=teamid)
    # load your chain
    llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
    chain = load_qa_chain(llm, chain_type="stuff")

    # set your query
    query = query
    # search for similar documents
    docs = docsearch.similarity_search(query, include_metadata=True)

    # run your chain
    result =chain.run(input_documents=docs, question=query)
    
    end = time.time()
    print(end - start)
    return result
   
