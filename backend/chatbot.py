import google.generativeai as genai

# 🔐 Set your Gemini API key directly here
genai.configure(api_key="AIzaSyBI0YYq-qAVdsx5i08ox-dciaYb_vWgC2A")  # Replace with your Gemini key

model = genai.GenerativeModel('gemini-pro')

# Keep chunks in memory
pdf_text_chunks = []

def set_chunks(chunks):
    global pdf_text_chunks
    pdf_text_chunks = chunks

def process_query(query):
    if not pdf_text_chunks:
        return "No PDF uploaded yet."

    # Join all chunks as context (for now, just simple concatenation)
    context = "\n".join(pdf_text_chunks)

    prompt = f"""You are an assistant. Here is the document content:\n{context}\n\nAnswer this question:\n{query}"""

    response = model.generate_content(prompt)
    return response.text
