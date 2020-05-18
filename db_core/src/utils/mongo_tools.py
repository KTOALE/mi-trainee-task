from functools import wraps
from pymongo import MongoClient
from settings import mongo_conn


def open_mongo_session(db_name):
    def inner_func(func):
        @wraps(func)
        def inner(*args, **kwargs):
            with MongoClient(**mongo_conn) as client:
                db = client[db_name]
                return func(db, *args, **kwargs)

        return inner

    return inner_func


@open_mongo_session("secrets_database")
def init_mongo(db):
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
def save_secret(db, data_to_save):
    pass


@open_mongo_session("secrets_database")
def load_secret(db, data_to_check):
    pass


if __name__ == "__main__":
    init_mongo()
