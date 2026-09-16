# Windows kompyuterida botni doimiy ishlatish

Bot Telegram bilan "polling" usulida ishlaydi — ya'ni tashqaridan kiruvchi
ulanish (port ochish, statik IP) kerak emas, kompyuteringiz internetga ulangan
va yoniq bo'lsa yetarli.

## 1-qadam: Python o'rnatish

Agar hali o'rnatilmagan bo'lsa: https://www.python.org/downloads/ dan yuklab
oling. O'rnatish oynasida albatta **"Add python.exe to PATH"** katagini
belgilang.

Tekshirish uchun `cmd` oching va yozing:
```
python --version
```

## 2-qadam: ffmpeg o'rnatish (ovozni tanish uchun SHART)

Eng oson yo'li — agar Windows 10/11 bo'lsa, `cmd`da:
```
winget install ffmpeg
```
Agar `winget` ishlamasa: https://www.gyan.dev/ffmpeg/builds/ dan
"release essentials" arxivini yuklab oling, biror joyga (masalan
`C:\ffmpeg`) chiqaring, so'ng `C:\ffmpeg\bin` papkasini Windows PATH
o'zgaruvchisiga qo'shing (Search → "Edit the system environment variables" →
Environment Variables → Path → New).

Tekshirish:
```
ffmpeg -version
```

## 3-qadam: Loyihani sozlash

`objektivka_bot` papkasini masalan `C:\objektivka_bot` ga joylashtiring,
so'ng `cmd`da:
```
cd C:\objektivka_bot
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

`.env.example` faylidan nusxa olib `.env` nomida saqlang va ichiga
haqiqiy bot tokeningizni yozing:
```
BOT_TOKEN=123456789:ABCDEF...
```

## 4-qadam: Qo'lda sinab ko'rish

```
run_bot.bat
```
oynani ishga tushiring. Terminalda "Bot ishga tushdi..." chiqsa — Telegramda
botingizga `/start` yozib sinab ko'ring. Ishlasa, oynani yopmasdan davom
eting yoki keyingi qadamga o'ting.

## 5-qadam: Kompyuter uxlab qolmasligini ta'minlash

**Sozlamalar → System → Power & sleep**:
- "Screen" va "Sleep" — ikkalasini ham **"Never"** qiling
  (kamida quvvat manbaiga ulangan holatda).

Noutbuk bo'lsa, qopqog'ini yopganda o'chib qolmasligi uchun:
**Control Panel → Power Options → Choose what closing the lid does** →
"When I close the lid" → **"Do nothing"**.

## 6-qadam: Kompyuter yoqilganda bot avtomatik ishga tushishi

### Oddiy usul (login qilinganda ishga tushadi)
1. `Win + R` bosing, `shell:startup` deb yozib Enter bosing — Startup
   papkasi ochiladi.
2. `run_bot.bat` faylining **yorlig'ini (shortcut)** shu papkaga joylashtiring
   (faylni o'ng tugma bilan bosib "Create shortcut", so'ng shortcutni
   Startup papkasiga ko'chiring).
3. Kompyuter yoqilib, sizning foydalanuvchi hisobingizga kirilganda (login
   qilinganda) bot avtomatik ishga tushadi.

> Eslatma: kompyuteringizni **avtomatik login** qiladigan qilib
> sozlasangiz (parolisiz yoki avto-logon), qayta yoqilganda ham hech kim
> qo'lda login qilmasa-da bot ishga tushadi.

### Mustahkamroq usul — Windows xizmati (service) sifatida (tavsiya etiladi)
Bu usulda bot **login qilmasdan ham**, fon rejimida ishlaydi va qulab
tushsa Windows o'zi avtomatik qayta tiklaydi:

1. https://nssm.cc/download dan **NSSM** dasturini yuklab oling, arxivdan
   `win64\nssm.exe` faylini masalan `C:\objektivka_bot\nssm.exe` ga
   joylashtiring.
2. `cmd`ni **Administrator** sifatida oching:
   ```
   cd C:\objektivka_bot
   nssm install ObjektivkaBot
   ```
3. Ochilgan oynada:
   - **Path**: `C:\objektivka_bot\venv\Scripts\python.exe`
   - **Startup directory**: `C:\objektivka_bot`
   - **Arguments**: `bot.py`
   - "Details" bo'limida **Startup type: Automatic**
   - "Install service" tugmasini bosing.
4. Xizmatni ishga tushirish:
   ```
   nssm start ObjektivkaBot
   ```
5. To'xtatish/o'chirish kerak bo'lsa:
   ```
   nssm stop ObjektivkaBot
   nssm remove ObjektivkaBot
   ```

Shu bilan bot kompyuter yoqilgan va internetga ulangan paytda doimiy
ishlab turadi — hech kim tizimga kirmasa ham.

## Muhim eslatmalar

- Internet uzilib qolsa, tiklangach bot o'zi qayta ulanadi (`run_bot.bat`
  yoki NSSM avtomatik qayta ishga tushiradi).
- Windows yangilanish sababli o'zi qayta yuklansa, NSSM usulida bot yana
  avtomatik ishga tushadi (login kutmasdan); `shell:startup` usulida esa
  faqat kimdir login qilgandan keyin ishga tushadi.
- Elektr uzilib qolishi mumkin bo'lgan joy bo'lsa, UPS (kichik quvvat
  manbai) bo'lishi tavsiya etiladi.
