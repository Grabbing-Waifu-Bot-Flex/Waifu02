import logging  

from pyrogram import Client 

from telegram.ext import Application
from motor.motor_asyncio import AsyncIOMotorClient

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

logging.getLogger("apscheduler").setLevel(logging.ERROR)
logging.getLogger('httpx').setLevel(logging.WARNING)
logging.getLogger("pyrate_limiter").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

OWNER_ID = "6584789596"
sudo_users = ["6584789596", "6154972031", "6100011620", "5702598840", "6101457748", "2010819209", "6764240805", "6584789596"]
GROUP_ID = "-1002000314620"
TOKEN = "7067713339:AAGB3tSBfrrh1wHKuDmKthKqxLWKmi7HdNI"
mongo_url = "mongodb+srv://Srikanta:srikanta@cluster0.xzbil3m.mongodb.net/?retryWrites=true&w=majority"
PHOTO_URL = ["https://telegra.ph//file/e64337bbc6cdac7e6b178.jpg", "https://telegra.ph/file/ed23556d07d33db18402d.jpg"]
SUPPORT_CHAT = "Grabbing_Your_WH_Group"
UPDATE_CHAT = "Grabbing_Your_WH_Channel"
BOT_USERNAME = "Testing_Opx_bot"
CHARA_CHANNEL_ID = "-1002000314620"
api_id = "24089031"
api_hash = "0615e3afe13ddaaf8e9ddbd3977d35ff"

application = Application.builder().token(TOKEN).build()
Grabberu = Client("Grabber", api_id, api_hash, bot_token=TOKEN)
client = AsyncIOMotorClient(mongo_url)
db = client['Character_catcher']
collection = db['anime_characters']
user_totals_collection = db['user_totals']
user_collection = db["user_collection"]
group_user_totals_collection = db['group_user_total']
top_global_groups_collection = db['top_global_groups']