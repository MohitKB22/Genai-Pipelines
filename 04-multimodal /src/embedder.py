class Embedder:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        from sentence_transformers import SentenceTransformer
        self.model = SentenceTransformer(model_name)

    def embed(self, texts):
        return self.model.encode(texts, convert_to_tensor=True)