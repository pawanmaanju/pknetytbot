import os

class Config:
    API_ID = int(os.getenv("API_ID", "21174134"))  # API ID as environment variable or default
    API_HASH = os.getenv("API_HASH", "3d7f8c4ee4978228f411bbd04f2eea73")  # API Hash as environment variable or default
    BOT_TOKEN = os.getenv("BOT_TOKEN", "7168358367:AAH21vD3sNQIMiV_Qg9NfG0VO1OI81-hdec")  # Bot Token
