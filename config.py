from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("33194036", 0))
        self.API_HASH = getenv("1086e25ee52f83c21d22939d3fbeaa89")

        self.BOT_TOKEN = getenv("8302819078:AAFXgriFJo8_lkgWNnpt68fY8pjhz6q8BiQ")
        self.MONGO_URL = getenv("mongodb+srv://sagarkaruna21_db_user:MACHAMUSICBOT@cluster0.xuasrtz.mongodb.net/?appName=Cluster0")

        self.LOGGER_ID = int(getenv("1003932641652", 0))
        self.OWNER_ID = int(getenv("757766615", 0))

        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60)) * 60
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))

        self.SESSION1 = getenv("BQH6gDQAis2Xz3KQMBhCY1GcJ6P_30Y_2N4UxSUD9mXfYLfGPdoEJM3F6EKEUK-csJbkG6OWgq5TvdorYtjcsAmY27-N1g5RbVfW1YNzXLR-oPOMk300sJ0w4yt8mxyhzz-BAoINzRMCzTl8XrMQwZ1XtCGM-S7sr4IpQrm8nKwzA2F09CrDDZpsm7u8Pk_LEWnj4AoXZ2JVXNTxoQN1nTynTiTOnwhcc58SO_xkq36Pdt5QKXktJF5bwG1Dpmn4hqAxjwqquTrLN5ylrlCvwEg4rps7pT4btErj8pvzAu3iyAYBYdf9MbNkyX09U6Jl0M0_dmqWaxVsqR_vHtMO2OcMaPcV5wAAAAGLZQOmAA", None)
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/machamusiccc")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+H3HAqM5zuYo0ODk1")

        self.API_URL = getenv("API_URL", "https://pvtz.nexgenbots.xyz")
        self.VIDEO_API_URL = getenv("VIDEO_API_URL", "https://api.video.nexgenbots.xyz")
        self.API_KEY = getenv("API_KEY", "30DxNexGenBots7fG9kL") # Get this value from https://console.nexgenbots.xyz

        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", "False").lower() == "true"
        self.AUTO_END: bool = getenv("AUTO_END", "False").lower() == "true"
    
        self.THUMB_GEN: bool = getenv("THUMB_GEN", "True").lower() == "true"
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", "True").lower() == "true"
        self.LANG_CODE = getenv("LANG_CODE", "en")

        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://te.legra.ph/file/3e40a408286d4eda24191.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/haagg2.png")
        self.START_IMG = getenv("START_IMG", "https://files.catbox.moe/zvziwk.jpg")

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
