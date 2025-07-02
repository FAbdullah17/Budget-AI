# 💰 Budget-AI

A smart AI assistant that helps you analyze your **bank statements** or answer **financial questions** using contextual understanding from an LLM and optionally vector search (RAG). Combines **LLaMA3 via Groq**, **FastAPI**, **ChromaDB**, and **a simple web UI**.

---

## 🚀 Features

- 🧾 Upload CSV/Excel bank statements
- ❓ Ask financial questions (e.g., “Why am I overspending?”)
- 🤖 LLM-powered reasoning via Groq’s LLaMA3
- 📊 Transaction summary with insights
- 🧠 RAG-enabled question answering (from `personal_finance_guide.txt`)
- 🌐 Optional Web Search Fallback
- 🌐 FastAPI-based backend + HTML/CSS UI

---

## 📁 Project Structure

```bash
Budget-AI/
│
├── examples/
│   └── bank_transactions.csv         # Sample 6-month transaction file
│
├── knowledge_base/
│   └── personal_finance_guide.txt   # Knowledge source for RAG
│
├── scripts/
│   ├── main.py                      # FastAPI entrypoint
│   ├── qa_engine.py                 # Question answering logic
│   ├── llm_config.py                # Groq LLaMA3 config
│   ├── rag_engine.py                # Vector DB setup (ChromaDB)
│   ├── utils.py                     # CSV summary logic
│   └── web_search.py                # (Optional) Web search fallback
│
├── static/
│   ├── index.html                   # Frontend UI
│   └── style.css                    # UI styling
│
├── uploads/                         # User-uploaded files
│
├── .env                             # Contains your GROQ_API_KEY
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repo

```bash
git clone https://github.com/yourusername/Budget-AI.git
cd Budget-AI
```

### 2. Create Environment

```bash
python -m venv venv
venv\Scripts\activate       # On Windows
source venv/bin/activate      # On Mac/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## 🧠 Usage

### 💻 Start the Server

```bash
uvicorn scripts.main:app --reload
```

Then open your browser:

```
http://127.0.0.1:8000
```

---

## 💬 Example Prompts

> “How can I reduce my monthly expenses?”

> “Why am I spending more than I earn?”

> “What’s my top spending category?”

---

### 📘 Real-Time Insights

From:
- Uploaded **bank file**
- Or contextual documents via RAG (`personal_finance_guide.txt`)
- Or live web search fallback (optional)

---

## 🛠 Developer Notes

### 🔍 Vector Store (RAG)

- `rag_engine.py` builds ChromaDB using `all-MiniLM-L6-v2` from HuggingFace.
- File indexed: `knowledge_base/personal_finance_guide.txt`
- Splitting: `RecursiveCharacterTextSplitter(chunk_size=500, overlap=50)`

### 🧠 LLM Integration

- Powered by **Groq's LLaMA3 70B**.
- API Base: `https://api.groq.com/openai/v1`
- Prompting: `{context} + {question}` → `llm_config.ask_llm()`

### 🌍 Web Search (Optional)

- `web_search.py` fallback to **DuckDuckGo** (can integrate SerpAPI if needed).

---

## 🎨 UI/UX Highlights

- Basic HTML + CSS form (`index.html`)
- Upload CSV/Excel + Ask a question
- JS Fetch API handles `/process` POST
- Results displayed in `<div id="result-text">`

---

## 🧪 Sample Output

> Input file: `examples/bank_transactions.csv`

Output:

```
Total Spent: $4,509.20
Total Received: $2,970.00
Average Transaction: -$90.65
Top Spending Categories:
- Healthcare
- Shopping
- Education
```

---

## 📄 License

[MIT License](LICENSE)

---

## 🤝 Contributions Welcome!

Open issues, submit PRs, or suggest new features. Budget-AI is still evolving!

---

## 📬 Contact

**Developer**: [Fahad Abdullah](mailto:fahadai.co@gmail.com)  
**GitHub**: [github.com/FahadAbdullah](https://github.com/FAbdullah17)