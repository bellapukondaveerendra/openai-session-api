from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get MongoDB connection URI
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client["openai_sessions"]  # Replace 'openai_sessions' with your preferred DB name
sessions_collection = db["sessions"]  # Collection to store session data
