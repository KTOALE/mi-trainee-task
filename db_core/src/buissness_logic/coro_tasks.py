from json import loads
from utils.mongo_tools import save_secret, load_secret


async def set_secret(msg):
    try:
        print(f"subject event: {msg.subject}")
        data_to_save = loads(msg.data)
        save_secret(data_to_save)
    except Exception as e:
        print(f"Error happens: {e}")


async def get_secret(msg):
    try:
        print(f"subject event: {msg.subject}")
        data_to_load = loads(msg.data)
        load_secret(data_to_load)
    except Exception as e:
        print(f"Error happens: {e}")
