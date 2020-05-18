from utils.mongo_tools import save_secret, load_secret


async def set_secret(msg):
    print(f"subject event: {msg.subject}")
    data_to_save = {}
    save_secret(data_to_save)


async def get_secret(msg):
    print(f"subject event: {msg.subject}")
    data_to_load = {}
    load_secret(data_to_load)
