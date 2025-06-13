# chatbot.py
import google.generativeai as genai

genai.configure(api_key="AIzaSyBI0YYq-qAVdsx5i08ox-dciaYb_vWgC2A")  # Replace with actual Gemini API key

# Global list to store PDF chunks
pdf_text_chunks = []

def set_chunks(chunks):
    """Set the PDF text chunks globally."""
    pdf_text_chunks.clear()
    pdf_text_chunks.extend(chunks)

def process_query(query: str):
    if not pdf_text_chunks:
        return "No PDF content found. Please upload a PDF first."

    prompt = "\n".join(pdf_text_chunks) + f"\n\nUser query: {query}"

    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating response: {e}"
