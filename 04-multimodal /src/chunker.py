class Chunker:
    def __init__(self, chunk_size=500, overlap=50):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk_text(self, text):
        """
        Splits the input text into overlapping chunks.

        Args:
            text (str): The text to be chunked.

        Returns:
            list: A list of text chunks.
        """
        chunks = []
        start = 0
        while start < len(text):
            end = start + self.chunk_size
            chunk = text[start:end]
            chunks.append(chunk)
            start += self.chunk_size - self.overlap
        return chunks

    def chunk_documents(self, documents):
        """
        Processes a list of documents and returns their chunks.

        Args:
            documents (list): A list of documents to be chunked.

        Returns:
            list: A list of chunked documents.
        """
        all_chunks = []
        for doc in documents:
            text = doc.page_content  # Assuming each document has a 'page_content' attribute
            chunks = self.chunk_text(text)
            all_chunks.extend(chunks)
        return all_chunks