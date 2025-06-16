# InsuraAI – AI-Powered Health Insurance Explainer

InsuraAI is a web-based tool that simplifies complex health insurance documents using Google’s Gemini AI. Users can upload any health insurance PDF and ask natural-language questions to get clear, personalized answers — no jargon, no confusion.

---

## 🔗 Live Demo

**[Try the Live App Here](https://ai-powered-health-insurance.onrender.com)**  
> ⚠️ *Note: Since the app is deployed on Render’s free tier, it may take 30–40 seconds to load initially.*

---

## 📄 Sample PDF

To help you test the app quickly, we've included a **sample health insurance PDF** in this repository:  
`/sample_health_insurance.pdf`

You can upload it to see how the AI explains policy clauses, benefits, exclusions, and more.

---

## 🧠 Key Features

- Upload any health insurance PDF
- Automatically extracts & embeds policy content
- Ask any insurance-related question
- Responses powered by Google's Gemini API
- Built with FastAPI, LangChain, and vanilla JavaScript
- Deployed using Render

---

## 💻 Tech Stack

- **Frontend:** HTML, CSS, Vanilla JavaScript  
- **Backend:** FastAPI, LangChain, PDFPlumber  
- **AI:** Google Gemini Pro (via GenerativeAI API)  
- **Deployment:** Render  
- **Document Parsing:** PDFPlumber

---

## 🚀 How It Works

1. Upload your health insurance policy in PDF format.
2. The backend parses the file, splits the content into chunks, and stores it in-memory for semantic search.
3. Ask any natural-language question via the chat interface.
4. Gemini AI responds with a user-friendly explanation based on the uploaded policy.

---

## 📦 Local Setup

```bash
git clone https://github.com/your-username/insuraai.git
cd insuraai/backend
python -m venv vnev
source vnev/bin/activate   # Windows: vnev\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
