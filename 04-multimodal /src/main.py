import os
from dotenv import load_dotenv
from document_loader import DocumentLoader
from chunker import Chunker
from embedder import Embedder
from vector_store import VectorStore
from retriever import Retriever
from generator import Generator

def main():
    # Load environment variables
    load_dotenv()
    
    # Initialize components
    document_loader = DocumentLoader()
    chunker = Chunker()
    embedder = Embedder()
    vector_store = VectorStore()
    retriever = Retriever(vector_store)
    generator = Generator()

    # Step 1: Load documents
    documents = document_loader.load_documents('Bentley Brouchure.pdf')
    
    # Step 2: Chunk documents
    chunks = chunker.chunk_documents(documents)
    
    # Step 3: Embed chunks
    embeddings = embedder.embed_chunks(chunks)
    
    # Step 4: Index embeddings
    vector_store.index_embeddings(embeddings)
    
    # Main loop for user queries
    while True:
        user_query = input("Ask a question (or type 'exit' to quit): ")
        if user_query.lower() == 'exit':
            break
        
        # Step 5: Retrieve relevant chunks
        relevant_chunks = retriever.retrieve(user_query)
        
        # Step 6: Generate answer
        answer = generator.generate_answer(relevant_chunks, user_query)
        
        print(f"Answer: {answer}")

if __name__ == "__main__":
    main()