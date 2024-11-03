import os
from pinecone import Pinecone, ServerlessSpec

# Define API key and index parameters
key = '4641190a-7251-4ae2-8ecd-b17623ecd3ae'
index_name = "vid-embeddings"
dimension = 3  # Now using 3 dimensions for vectors

# Create an instance of the Pinecone class
pc = Pinecone(api_key=key)

# Delete the old index (optional, only if it already exists)
if index_name in pc.list_indexes().names():
    pc.delete_index(index_name)

# Create the index with 3 dimensions
pc.create_index(
    name=index_name,
    dimension=dimension,
    metric="cosine",  # Using cosine similarity for similarity search
    spec=ServerlessSpec(
        cloud="aws",  # Cloud provider
        region="us-east-1"  # Specify the region
    )
)

# Connect to the new index
index = pc.Index(index_name)

# Example 3-dimensional vectors (using floats)
vectors = [
    ('test1', [1.0, 2.0, 3.0]),  # A vector with 3 dimensions
    ('test2', [2.0, 2.0, 2.0]),
    ('test3', [3.0, 4.0, 3.0])
]

# Upsert (add or update) vectors to the index
index.upsert(vectors)

# Optional: Check list of indexes
print("Available indexes:", pc.list_indexes().names())

print("testing")