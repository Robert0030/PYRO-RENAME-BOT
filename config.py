import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "27884084")

API_HASH = os.environ.get("API_HASH", "f41ef10f7e283ba0b6b18fac6fbe8226")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5680057689:AAFLaqV6MkPJQ1SIXuSZTasBG_jfcHpGtuk") 

FORCE_SUB = os.environ.get("FORCE_SUB", "movierequestgroupl") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://MrStark:20urcm06@cluster0.qhcpkym.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/3583efe74f1b3179b7640.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN',1899869233 '').split()]

