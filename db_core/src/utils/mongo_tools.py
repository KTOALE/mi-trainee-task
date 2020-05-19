from functools import wraps
from pymongo import MongoClient
from pymongo.database import Database
from settings import mongo_conn


def open_mongo_session(db_name):
    def inner_func(func):
        @wraps(func)
        def inner(*args, **kwargs):
            with MongoClient(**mongo_conn) as client:
                db = client[db_name]
                print(f"db type:{type(db)}")
                return func(db, *args, **kwargs)

        return inner

    return inner_func


@open_mongo_session("secrets_database")
def init_mongo(db: Database):
    db["secrets"].insert_one({
        "email": "root",
        "secret_phrase": "",
        "secret": "",
    })
    db["users"].insert_one({
        "email": "root@home.org",
        "password": "1234qwer"
    })


@open_mongo_session("secrets_database")
def save_secret(db: Database, data_to_save):
    db["secrets"].insert_one({
        "email": data_to_save.get("email"),
        "secret_phrase": data_to_save.get("secret_phrase"),
        "secret": data_to_save.get("secret"),
    })


@open_mongo_session("secrets_database")
def load_secret(db: Database, data_to_check):
    pass


if __name__ == "__main__":
    init_mongo()
