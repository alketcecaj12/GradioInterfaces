# 🖥️ GradioInterfaces

> A practical progression from Gradio's simple `Interface` API to the full `Blocks` API — built around a real-world pattern: **upload a document, ask a question, get an LLM-powered answer, and route the output downstream**.

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Gradio](https://img.shields.io/badge/Gradio-4.x-FF6B35?style=flat-square&logo=gradio&logoColor=white)
![LLM Ready](https://img.shields.io/badge/LLM-API--Ready-6366f1?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)

---

## 📌 What Is This?

Two self-contained Gradio apps that implement **LLM-powered document Q&A** with increasing sophistication:

| File | API Style | Key Feature |
|---|---|---|
| `app.py` | `gr.Interface` | Minimal — upload file, ask question, get answer |
| `app_v2.py` | `gr.Blocks` | Full layout — Q&A + downstream API output routing |

The pattern is directly applicable to RAG pipelines, internal document search tools, audit report Q&A, and any workflow where a user needs to interrogate text via an LLM and optionally push the result to another system.

---

## 🏗️ Architecture

### `app.py` — Minimal Q&A Interface

```
┌─────────────────────────────────────┐
│          gr.Interface               │
│                                     │
│  [Upload Text File]  [Ask a Question] │
│            │               │        │
│            └──────┬────────┘        │
│                   ▼                 │
│         query_llm_api(context, q)   │
│                   │                 │
│                   ▼                 │
│              [Answer Box]           │
└─────────────────────────────────────┘
```

### `app_v2.py` — Full Blocks Layout with Output Routing

```
┌──────────────────────────────────────────┐
│              gr.Blocks                   │
│                                          │
│  ┌──────────────────┬─────────────────┐  │
│  │ Upload Text File │ Ask a Question  │  │
│  └──────────────────┴─────────────────┘  │
│                  [Submit]                │
│                     │                   │
│                     ▼                   │
│           query_llm_api(context, q)     │
│                     │                   │
│                     ▼                   │
│              [Answer Box]               │
│                     │                   │
│          [Send Output to API]           │
│                     │                   │
│                     ▼                   │
│         PUT → YOUR_PUT_API_ENDPOINT     │
│                     │                   │
│              [API Response]             │
└──────────────────────────────────────────┘
```

---

## 🚀 Quickstart

```bash
# Clone
git clone https://github.com/alketcecaj12/GradioInterfaces.git
cd GradioInterfaces

# Install dependencies
pip install gradio requests

# Run v1 (simple interface)
python app.py

# Run v2 (full Blocks layout)
python app_v2.py
```

The app launches at `http://localhost:7860` by default.

---

## ⚙️ Configuration

Before running, set your LLM API credentials in the relevant file:

```python
# In app.py or app_v2.py
api_endpoint = "YOUR_API_ENDPOINT"   # e.g. https://api.openai.com/v1/chat/completions

headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}
```

For `app_v2.py`, also configure the downstream PUT endpoint:

```python
api_endpoint = "YOUR_PUT_API_ENDPOINT"  # e.g. https://your-system/api/results
```

> **Tip:** Use environment variables in production — never hardcode keys in source files.
>
> ```python
> import os
> api_key = os.environ.get("LLM_API_KEY")
> ```

---

## 🔍 v1 vs v2 — What Changed?

| Feature | `app.py` | `app_v2.py` |
|---|---|---|
| Gradio API | `gr.Interface` | `gr.Blocks` |
| Layout control | Auto | Manual rows + columns |
| Submit trigger | Auto | Explicit button |
| Output routing | ❌ | ✅ PUT to downstream API |
| Extensibility | Low | High |

`gr.Interface` is ideal for quick prototypes. `gr.Blocks` is the production pattern — it gives full control over layout, event wiring, and multi-step workflows.

---

## 💡 Use Cases

This pattern maps directly onto several real-world scenarios:

- **Document Q&A** — upload a policy, contract, or report and query it with natural language
- **RAG front-end** — drop in a retrieval endpoint behind `query_llm_api` for grounded answers
- **Audit tooling** — upload audit findings, ask structured questions, export results to a case management system
- **Internal search** — lightweight alternative to a full search stack for small document collections

---

## 🧩 Extending the Apps

A few natural next steps:

```python
# 1. Support PDF uploads (not just plain text)
import pdfplumber

def extract_text(file):
    with pdfplumber.open(file.name) as pdf:
        return "\n".join(p.extract_text() for p in pdf.pages)

# 2. Add streaming output
# Use gr.Textbox with streaming=True and yield from your API call

# 3. Multi-file support
# Wrap file reading in a loop and concatenate contexts

# 4. Swap in a local model (Ollama)
# Replace api_endpoint with http://localhost:11434/api/generate
```

---

## 📁 Repository Structure

```
GradioInterfaces/
├── app.py          # v1 — gr.Interface, minimal Q&A
├── app_v2.py       # v2 — gr.Blocks, Q&A + output routing
├── img.png         # Screenshot of the interface
└── README.md
```

---

## 👤 Author

**Alket Cecaj, PhD** — Data Scientist & Quantitative Risk Analyst  
12+ years in data science · Copenhagen 🇩🇰

[![GitHub](https://img.shields.io/badge/GitHub-alketcecaj12-181717?style=flat-square&logo=github)](https://github.com/alketcecaj12)

---

## 📄 License

MIT — free to use, adapt, and build on.

---

> *The best interface is the one that gets out of the way. Gradio does that. This repo shows how.*
