# Ob'ektivka (МАЪЛУМОТНОМА) Telegram-bot

Bu bot foydalanuvchidan savollarni **matn** ko'rinishida so'raydi, foydalanuvchi
esa **ovozli xabar** bilan javob beradi. Ovoz avtomatik matnga aylantiriladi,
foydalanuvchi natijani tasdiqlaydi yoki xato bo'lsa qo'lda tuzatadi. Oxirida
rasm so'raladi va tayyor `.docx` ob'ektivka fayli yuboriladi.

## Botning ish tartibi

1. `/start` — til tanlanadi: **Lotin** yoki **Кирилл**.
2. Oddiy maydonlar birma-bir so'raladi (F.I.SH., tug'ilgan sana, millati,
   ma'lumoti va h.k.). Ilmiy daraja, ilmiy unvon, davlat mukofotlari,
   deputatlik kabi ko'pincha "yo'q" bo'ladigan savollarda **"❌ Yo'q"** tez
   tugmasi chiqadi — bosilsa, ovoz kerak emas.
3. **Mehnat faoliyati**: har bir bosqich uchun "qachondan", "qachongacha",
   "qayerda va kim bo'lib" alohida-alohida so'raladi, so'ng "yana
   qo'shasizmi?" tugmasi bilan davom ettirish yoki tugatish mumkin.
4. **Yaqin qarindoshlar**: ota va ona har doim so'raladi. Aka, uka, opa,
   singil — "bormi?" deb so'raladi, bo'lsa nechta bo'lsa ham "yana
   qo'shasizmi?" tugmasi bilan qo'shiladi. **Turmush o'rtog'i "yo'q"**
   deyilsa, farzand, qaynona, qaynota haqida umuman savol berilmaydi.
   Turmush o'rtog'i bor bo'lsa, ular ham so'raladi (farzand uchun avval
   qizi/o'g'li tanlanadi).
5. Oxirida rasm (3x4 yoki istalgan) **photo** sifatida so'raladi.
6. Shundan so'ng bot `.docx` fayl generatsiya qilib, foydalanuvchiga yuboradi.

Har bir ovozli javobdan keyin bot tanigan matnni ko'rsatadi va
**✅ Tasdiqlash** / **✏️ Qayta yozish** tugmalarini chiqaradi — "Qayta
yozish" bosilsa, keyingi yozgan matn to'g'ridan-to'g'ri javob sifatida
qabul qilinadi (ASR xatosini qo'lda tuzatish imkoniyati).

## O'rnatish

Bot ikki xil rejimda ishlashi mumkin (kod bir xil — faqat sozlama farq qiladi):

- **Polling** — uy kompyuterida yoki o'z serveringizda ishlatish uchun.
  Qadam-baqadam: **`WINDOWS_SETUP.md`**.
- **Webhook** — Render.com kabi bepul, karta so'ramaydigan hostingda
  ishlatish uchun (tavsiya etiladi, agar Oracle/VPS mos kelmasa).
  Qadam-baqadam: **`RENDER_SETUP.md`**.

### 1. Talablar
- Python 3.10+
- **ffmpeg** (ovozni `.ogg`dan `.wav`ga aylantirish uchun shart)
  - Ubuntu/Debian: `sudo apt install ffmpeg`
  - Windows: https://ffmpeg.org/download.html dan yuklab, PATHga qo'shing
  - macOS: `brew install ffmpeg`
- Internet aloqasi (Telegram API va Google Speech API uchun)

### 2. Bot tokenini olish
1. Telegramda **@BotFather** ga yozing.
2. `/newbot` buyrug'ini yuboring, nom va username bering.
3. Sizga beriladigan tokenni saqlab qo'ying.

### 3. Loyihani ishga tushirish
```bash
cd objektivka_bot
python -m venv venv
source venv/bin/activate        # Windowsda: venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env
# .env faylni ochib, BOT_TOKEN= qatoriga haqiqiy tokeningizni yozing

python bot.py
```
Terminalda `Bot ishga tushdi...` degan yozuv chiqsa, bot Telegramda ishlay
boshlagan bo'ladi.

## Muhim eslatmalar

- **Ovozni matnga aylantirish (Google Speech Recognition, bepul)**: bu
  xizmat rasmiy ravishda o'zbek tilini qo'llab-quvvatlamaydi, shuning uchun
  ba'zan noaniq natija berishi mumkin — aynan shuning uchun bot har doim
  tasdiqlash/tuzatish bosqichini o'z ichiga oladi. Agar sifat qoniqarsiz
  bo'lsa, kelajakda `transcribe.py` faylida boshqa xizmatga (masalan,
  Yandex SpeechKit yoki OpenAI Whisper API) osongina o'tish mumkin —
  faqat `transcribe_ogg()` funksiyasini almashtirish kifoya.
- Bot bir vaqtning o'zida bir nechta foydalanuvchi bilan ishlashi mumkin
  (har bir foydalanuvchi holati alohida saqlanadi), lekin ma'lumotlar
  botning xotirasida (RAM) saqlanadi — bot qayta ishga tushirilsa, tugallanmagan
  suhbatlar yo'qoladi.
- Savollar matni, maydonlar tartibi va hujjat ko'rinishini o'zgartirish
  uchun **`texts.py`** (savollar/lейбллар) va **`doc_builder.py`** (hujjat
  formati) fayllarini tahrirlang.

## Fayllar tuzilishi

```
objektivka_bot/
├── bot.py            — asosiy bot logikasi (suhbat oqimi)
├── texts.py           — barcha savollar, lейбллар, tugma matnlari (lat/cyr)
├── doc_builder.py     — yig'ilgan ma'lumotdan .docx hujjat yasaydi
├── transcribe.py       — ovozni matnga aylantirish
├── config.py           — sozlamalar (token, papkalar)
├── requirements.txt
├── .env.example
└── README.md
```
