from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from pdf_parser import extract_text_from_pdf
from chatbot import process_query, set_chunks

app = FastAPI()

# Enable CORS if you plan to connect frontend later
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_pdf(file: UploadFile):
    content = await file.read()
    chunks = extract_text_from_pdf(content)
    set_chunks(chunks)
    return {"message": "PDF processed", "chunks": len(chunks)}

@app.post("/chat")
async def chat(query: str = Form(...)):
    response = process_query(query)
    return {"response": response}
