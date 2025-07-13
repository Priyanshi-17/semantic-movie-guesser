import os
import json
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document
from langchain_community.embeddings import HuggingFaceEmbeddings


def load_json_data(filename):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
    filepath = os.path.join(base_dir, "data", filename)
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f) 

def create_documents(movie_data):
    docs = []
    for movie in movie_data:
        metadata = {
            "title": movie["title"],
            "industry": movie["industry"]
        }
        content = movie["storyline"]
        docs.append(Document(page_content=content, metadata=metadata))
    return docs

def build_faiss_index(docs, save_path):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local(save_path)
    print(f"FAISS index saved to {save_path}")

if __name__ == "__main__":
    os.makedirs("embeddings", exist_ok=True)

    #Converted movie plots into embeddings (vector form).
    # Bollywood + Tollywood
    print("🔥 Loading Bollywood+Tollywood Data...")
    bt_data = load_json_data("bollywood_tollywood.json")
    print("📄 Creating Bollywood+Tollywood Documents...")
    bt_docs = create_documents(bt_data)
    print("🧠 Building FAISS Index for Bollywood+Tollywood...")
    build_faiss_index(bt_docs, "embeddings/bollywood_tollywood_index")

    print("🔥 Loading Hollywood Data...")
    h_data = load_json_data("hollywood.json")
    print("📄 Creating Hollywood Documents...")
    h_docs = create_documents(h_data)
    print("🧠 Building FAISS Index for Hollywood...")
    build_faiss_index(h_docs, "embeddings/hollywood_index")

