import os
import openai
from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Keep FAISS index in memory
db = None

def process_query(query, chunks):
    global db
    if db is None:
        docs = [Document(page_content=chunk) for chunk in chunks]
        embedding = OpenAIEmbeddings()
        db = FAISS.from_documents(docs, embedding)

    retriever = db.as_retriever()
    qa = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model_name="gpt-4o"),
        chain_type="stuff",
        retriever=retriever
    )
    return qa.run(query)
