import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6966393837:AAG2Fa1OGddMggWNgnL")

    API_ID = int(os.environ.get("API_ID", 23995611))

    API_HASH = os.environ.get("API_HASH", "a1b94f10b912c9d732c320f9c73d73dc")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5631774748").split())

    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "https://t.me/jammesupdates")

    MAX_FILE_SIZE = 4194304000

    TG_MAX_FILE_SIZE = 4194304000

    FREE_USER_MAX_FILE_SIZE = 4194304000

    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))

    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")

    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    OUO_IO_API_KEY = ""

    MAX_MESSAGE_LENGTH = 4096

    PROCESS_MAX_TIMEOUT = 0

    DEF_WATER_MARK_FILE = "Use this bot @gugolxformebot"

    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://admin:12341234@cluster0.0xye2w3.mongodb.net/?retryWrites=true&w=majority")

    SESSION_NAME = os.environ.get("SESSION_NAME", "gugolxformebot)

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL",))

    LOGGER = logging

    OWNER_ID = int(os.environ.get("OWNER_ID", "5631774748"))

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "jammesupdates")
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "gugolxformebot)
