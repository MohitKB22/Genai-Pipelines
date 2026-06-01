# RAG from Scratch with OpenAI 🔍

This project is a step-by-step implementation of Retrieval-Augmented Generation (RAG) using LangChain, FAISS, and HuggingFace embeddings. It provides a beginner-friendly approach to building a system that enhances the capabilities of Large Language Models (LLMs) by allowing them to access specific documents at query time.

---

## What is RAG and Why Does It Matter?

**The problem with plain LLMs:** Large Language Models like GPT-4 are trained on data up to a certain cutoff date and do not have access to your private documents. This means they cannot answer specific questions about your company's policies, research papers, or product documentation.

**What RAG does:** RAG (Retrieval-Augmented Generation) addresses this limitation by providing LLMs with access to your documents during the query process. Instead of retraining the model, documents are stored in a searchable vector database. When a user asks a question, the most relevant passages are retrieved and included in the LLM's prompt, allowing it to generate answers based on your documents.

**Why it matters:** RAG is a leading architecture for production AI Q&A systems. It is cost-effective (no retraining), easily updatable (just add documents), and auditable (you can track which document chunks informed each answer). Understanding RAG from scratch equips you to build applications ranging from customer support bots to internal knowledge assistants.

---

## Project Structure

```
rag-from-scratch-openai/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── openai_client.py
│   ├── document_loader.py
│   ├── chunker.py
│   ├── embedder.py
│   ├── vector_store.py
│   ├── retriever.py
│   └── generator.py
├── data/
│   └── sample_docs/
├── tests/
│   ├── test_document_loader.py
│   └── test_retriever.py
├── notebooks/
│   └── exploration.ipynb
├── .env.example
├── requirements.txt
├── pyproject.toml
├── README.md
└── LICENSE
```

---

## Setup Instructions

### 1. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate         # Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure your API key

```bash
cp .env.example .env
```

Open `.env` and replace `your_openai_api_key_here` with your actual key from [platform.openai.com](https://platform.openai.com/api-keys).

### 4. Add your documents

Drop any `.pdf`, `.txt`, or `.docx` files into:

```
data/sample_docs/
```

### 5. Run the application

```bash
python src/main.py
```

---

## How to Verify the LLM Uses Your Documents

To ensure the system is reading your documents correctly, create a test document with specific information and query it. For example, if you have a document stating "The Zorbax Protocol was established in 2019 by Dr. Eleanor Voss," you can ask, "Who established the Zorbax Protocol?" and expect the correct response.

---

## Using the OpenAI API

This project utilizes the OpenAI API for generating answers. Ensure you have a valid API key and follow the configuration steps outlined above.

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

## Acknowledgments

Thanks to the LangChain, FAISS, and HuggingFace communities for their contributions to the tools used in this project.