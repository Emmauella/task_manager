from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# Connect to mongo Atlas Cluster
mongo_client = MongoClient("mongodb+srv://task_manager:task_manager@grow-cohort6.bpckwv8.mongodb.net/")

# Access database
task_manager_db = mongo_client["task_manager_db"]

# Pick a collection to operate On.
tasks = task_manager_db["tasks"]