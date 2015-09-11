#   database.py
#   Description:    ...

from pymongo import MongoClient
import configs

try:
    db_host = configs.DATABASE_HOST.strip()
    db_port = int(configs.DATABASE_PORT)
    db_name = configs.DATABASE_NAME.strip()

    client = MongoClient(db_host, db_port)
    db = client[db_name]

except:
    exit(1)
