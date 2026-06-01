import unittest
from src.retriever import Retriever
from src.vector_store import VectorStore
from src.embedder import Embedder

class TestRetriever(unittest.TestCase):
    def setUp(self):
        self.vector_store = VectorStore()
        self.embedder = Embedder()
        self.retriever = Retriever(self.vector_store)

    def test_retrieve_relevant_chunks(self):
        # Sample data for testing
        sample_chunks = [
            "The Zorbax Protocol was established in 2019 by Dr. Eleanor Voss.",
            "The protocol requires three phases: initialization, calibration, and review.",
            "The capital of Australia is Canberra."
        ]
        
        # Simulate adding chunks to the vector store
        for chunk in sample_chunks:
            vector = self.embedder.embed(chunk)
            self.vector_store.add(chunk, vector)

        # Test retrieval of relevant chunks
        query = "Who established the Zorbax Protocol?"
        retrieved_chunks = self.retriever.retrieve(query)

        self.assertIn("The Zorbax Protocol was established in 2019 by Dr. Eleanor Voss.", retrieved_chunks)

    def test_retrieve_no_relevant_chunks(self):
        # Test retrieval when no relevant chunks exist
        query = "What is the capital of France?"
        retrieved_chunks = self.retriever.retrieve(query)

        self.assertEqual(retrieved_chunks, [])

if __name__ == '__main__':
    unittest.main()