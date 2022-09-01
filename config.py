import pymongo
import certifi

connection_str = "mongodb+srv://EddieReynoso:ec00d8c6ac@cluster0.wuumrnl.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(connection_str, tlsCAFile = certifi.where())

db = client.get_database("EddieDataBase")