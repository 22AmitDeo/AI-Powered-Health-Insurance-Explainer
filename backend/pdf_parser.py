import pdfplumber
import io
from langchain.text_splitter import RecursiveCharacterTextSplitter

def extract_text_from_pdf(file_bytes):
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        full_text = ""
        for page in pdf.pages:
            full_text += page.extract_text() or ""

    # Chunk text using LangChain's splitter
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(full_text)
    return chunks
