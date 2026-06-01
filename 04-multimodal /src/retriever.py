class Retriever:
    def __init__(self, vector_store):
        self.vector_store = vector_store

    def retrieve(self, query, k=5):
        """
        Retrieve the top-k relevant document chunks for a given query.

        Parameters:
        - query (str): The user query to search for.
        - k (int): The number of top relevant chunks to retrieve.

        Returns:
        - List[Document]: A list of the top-k relevant document chunks.
        """
        query_embedding = self.vector_store.embed_query(query)
        return self.vector_store.search(query_embedding, k)