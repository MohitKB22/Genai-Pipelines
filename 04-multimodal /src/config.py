import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    FAISS_INDEX_PATH = os.getenv("FAISS_INDEX_PATH", "faiss_index/")
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 500))
    TOP_K = int(os.getenv("TOP_K", 3))