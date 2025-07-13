from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def load_vectorstore(index_path):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)

def test_index(index_path):
    vectorstore = load_vectorstore(index_path)
    docs = list(vectorstore.docstore._dict.values())
    print(f"📦 Index Path: {index_path}")
    print(f"🔍 Total Documents: {len(docs)}")

    if docs:
        print("✅ Sample Document:")
        doc = docs[0]
        print(f" - Title: {doc.metadata.get('title')}")
        print(f" - Storyline: {doc.page_content[:100]}...")
    else:
        print("❌ No documents found!")

# Test both
test_index("embeddings/bollywood_tollywood_index")
test_index("embeddings/hollywood_index")



