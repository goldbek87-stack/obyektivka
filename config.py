import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# Speech-to-text uchun til kodlari. Avval birinchisi sinaladi, ishlamasa
# navbatdagisi sinaladi. Google Web Speech API rasmiy ravishda o'zbek tilini
# qo'llab-quvvatlamaydi, shuning uchun ruscha kod zaxira sifatida qo'yilgan —
# lekin ko'p hollarda "uz-UZ" bilan ham urinib ko'rish natija beradi.
STT_LANGUAGES = ["uz-UZ", "ru-RU"]

# Vaqtinchalik fayllar (ovoz, rasm) saqlanadigan papka
TMP_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp")
os.makedirs(TMP_DIR, exist_ok=True)

# Tayyor hujjatlar saqlanadigan papka
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# --- Webhook rejimi (Render.com kabi hostinglar uchun) ---
# Agar WEBHOOK_HOST bo'sh bo'lsa -> oddiy "polling" rejimida ishlaydi
# (uy kompyuteri / VPS uchun mos). Agar to'ldirilsa (masalan
# https://sizning-botingiz.onrender.com) -> webhook rejimida ishlaydi.
WEBHOOK_HOST = os.getenv("WEBHOOK_HOST", "").rstrip("/")
PORT = int(os.getenv("PORT", "10000"))

