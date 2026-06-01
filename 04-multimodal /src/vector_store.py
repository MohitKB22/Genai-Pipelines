class VectorStore:
    def __init__(self, index_path: str):
        import faiss
        import numpy as np
        
        self.index_path = index_path
        self.index = self.load_index()

    def load_index(self):
        try:
            return faiss.read_index(self.index_path)
        except Exception as e:
            print(f"Failed to load index: {e}")
            return None

    def save_index(self):
        faiss.write_index(self.index, self.index_path)

    def add_vectors(self, vectors: np.ndarray):
        if self.index is None:
            raise ValueError("Index is not initialized.")
        self.index.add(vectors)

    def search(self, query_vector: np.ndarray, k: int = 5):
        if self.index is None:
            raise ValueError("Index is not initialized.")
        distances, indices = self.index.search(query_vector, k)
        return distances, indices

    def reset(self):
        self.index = faiss.IndexFlatL2(self.index.d)  # Reset to a new index
        self.save_index()  # Save the empty index if needed