from pymongo import MongoClient


    
client = MongoClient("mongodb://localhost:27017",
                                username="studentuser",
                                password="studentuser",
                                authSource="student",
                                authMechanism="SCRAM-SHA-1")

def check_if_db_exist():
    dblist = client.list_database_names()
    if "student" in dblist:
        print("The database exists.")
        db = client["student"]
    else:
        print("The database does not exists.")
        exit
    return db

def check_if_collection_exist():
    db = check_if_db_exist()
    collection_list = db.list_collection_names()
    if "student" in collection_list:
        print("The collection exists.")
        collection_student = db["student"]
    else:
        print("The collection does not exists.")
    return collection_student

def insert_student_details(student1):
    collection = check_if_collection_exist()
    x = collection.insert_one(student1)
    print(x.inserted_id)

def close_connection():
    client.close()
