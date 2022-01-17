import pymongo as pymongo

from mongodb_password import MONGO_DB_PASSWORD

db_client = pymongo.MongoClient(
    f"mongodb+srv://my770mongo:{MONGO_DB_PASSWORD}@cluster0.fbsnn.mongodb.net/default?retryWrites=true&w=majority")
tailor_med_db = db_client.tailor_med

patients_collections = tailor_med_db["patients"]
treatments_collections = tailor_med_db["treatments"]
