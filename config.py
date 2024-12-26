import os

class Config:
      BOT_TOKEN = os.environ.get("BOT_TOKEN", "7168358367:AAFB_QprJDdWGhf0-BLnTI-YzlJUNUS8hd4")
      API_ID = int(os.environ.get("API_ID",21174134 ))
      API_HASH = os.environ.get("API_HASH", "3d7f8c4ee4978228f411bbd04f2eea73")