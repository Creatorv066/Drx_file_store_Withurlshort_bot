import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "29406031"))
  API_HASH = os.environ.get("API_HASH", "83205ba993eac9cfc888387ac03e6688")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6840607964:AAGOoY_ofrG-Ep42cm8VUyrVILWR7pKDAwM")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "DRX_FiLE_STORE_BOT")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002197832722"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "modijiurl.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "fe930e58ec20ee01ad182f2f4320ff9149c44dc3")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "6690846736"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Cluster0:Cluster0@cluster0.kailvlv.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002054114895")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002088755828"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [𝐃𝐑𝐗](https://t.me/DRX_OFFICIALS_BOT)
 
 I am Super noob Please Support My Hard Work.

[𝐃𝐨𝐧𝐚𝐭𝐞 𝐌𝐞](https://t.me/DRX_OFFICIALS_BOT)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
