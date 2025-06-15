from fastapi import FastAPI, UploadFile, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from chatbot import process_query, set_chunks
from pdf_parser import extract_text_from_pdf

app = FastAPI()

# Serve static files (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# HTML templates
templates = Jinja2Templates(directory="templates")

# Optional CORS for external frontend (still safe to keep)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/upload", response_class=HTMLResponse)
async def upload_page(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

@app.get("/chat", response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

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
