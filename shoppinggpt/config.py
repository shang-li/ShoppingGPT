import os
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load environment variables from project .env if present
load_dotenv()

# API Keys
#GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Paths (prefer env overrides; fall back to repo-relative defaults)
DATA_DIR = os.getenv("DATA_DIR", os.path.join("data"))
DATA_PRODUCT_PATH = os.getenv("DATA_PRODUCT_PATH", os.path.join(DATA_DIR, "products.db"))
DATA_TEXT_PATH = os.getenv("DATA_TEXT_PATH", os.path.join(DATA_DIR, "policy.txt"))
STORE_DIRECTORY = os.getenv("STORE_DIRECTORY", os.path.join(DATA_DIR, "datastore"))

# Embeddings
# Use local Hugging Face sentence-transformers by default.
# Override with env var `HF_EMBEDDING_MODEL` to change model.
EMBEDDINGS = HuggingFaceEmbeddings(
    model_name=os.getenv("HF_EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
)
