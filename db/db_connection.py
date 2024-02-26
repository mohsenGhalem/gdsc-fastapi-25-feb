import os

import pymongo
from pymongo import MongoClient


def get_database():
    connection_string = os.environ.get('MONGO_CONNECTION_STRING')

    client = MongoClient(connection_string)

    return client['gdsc']


def close_db_connection():
    client = pymongo.MongoClient()
    client.close()