from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pdf_parser import extract_text_from_pdf
from chatbot import process_query 

app= FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pdf_text_chunks=[]

@app.post("/upload")
async def upload_pdf(file: UploadFile):
    content = await file.read()
    chunks = extract_text_from_pdf(content)
    global pdf_text_chunks
    pdf_text_chunks = chunks
    return {"message": "PDF processed", "chunks": len(chunks)}

@app.post("/chat")
async def chat(query: str = Form(...)):
    global pdf_text_chunks
    if not pdf_text_chunks:
        return {"response": "Please upload a PDF first."}
    answer = process_query(query, pdf_text_chunks)
    return {"response": answer}