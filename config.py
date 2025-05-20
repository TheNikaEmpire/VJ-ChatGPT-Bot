import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "29962141"))
API_HASH = environ.get("API_HASH", "27fcf227b58f85cedf46098b9c2ea240")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "2570967954"))
ADMINS = int(environ.get("ADMINS", "7483283743"))
DB_URI = environ.get("DB_URI", "mongodb+srv://thenikaempire:BMiN7Qou9Y94zau7@cluster0.00jz2ru.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "chatgptvjbot")
OPENAI_API = environ.get("OPENAI_API", "")
AI = is_enabled((environ.get("AI","True")), False)
