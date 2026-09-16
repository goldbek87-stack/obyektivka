# Render.com'da joylashtirish (karta so'ramaydi)

Bu usul Oracle Cloud'dagi kabi karta talab qilmaydi — faqat email va GitHub
hisobingiz bo'lsa yetarli. Bot **webhook** rejimida ishlaydi (bot.py buni
avtomatik qo'llab-quvvatlaydi — `WEBHOOK_HOST` sozlansa webhook, sozlanmasa
polling rejimida ishlaydi).

> Eslatma: Render'ning bepul tarifida servis 15 daqiqa harakatsiz qolsa
> "uxlab qoladi" va keyingi xabarga sekinroq (10-30 soniya) javob beradi.
> Buni oldini olish uchun oxirida **UptimeRobot** sozlaymiz — u har 5
> daqiqada botga "ping" yuborib, uni doim uyg'oq ushlab turadi.

## 1-qadam: Kodni GitHub'ga yuklash

1. https://github.com da yangi (bo'sh) repository yarating, masalan
   `objektivka-bot` nomi bilan (Public yoki Private — farqi yo'q).
2. Shu papkadagi barcha fayllarni (`objektivka_bot` ichidagi hammasini)
   o'sha repository'ga yuklang. Buning uchun GitHub saytida
   "Add file → Upload files" orqali barcha fayl/papkalarni sudrab
   tashlashingiz mumkin (`.env` faylini **yuklamang** — u yerda tokeningiz
   bor, xavfsizlik uchun).

## 2-qadam: Render'da hisob ochish

1. https://render.com ga kiring, **"Get Started"** → GitHub hisobingiz
   orqali ro'yxatdan o'ting (karta so'ramaydi).
2. Render'ga GitHub repositoryingizga ruxsat bering.

## 3-qadam: Web Service yaratish

1. Render dashboard'da **"+ New" → "Web Service"** ni bosing.
2. Repository ro'yxatidan `objektivka-bot` ni tanlang (Connect).
3. Sozlamalarni to'ldiring:
   - **Name**: `objektivka-bot` (yoki xohlagan nom)
   - **Environment**: **Docker** ni tanlang (repositoryda `Dockerfile`
     bor — Render uni avtomatik topib, ffmpeg bilan birga o'rnatadi)
   - **Instance Type**: **Free ($0/month)**
4. **"Environment Variables"** bo'limida quyidagilarni qo'shing:

   | Key | Value |
   |---|---|
   | `BOT_TOKEN` | @BotFather'dan olgan haqiqiy tokeningiz |
   | `WEBHOOK_HOST` | hozircha `https://vaqtinchalik.com` deb yozing (keyingi qadamda to'g'irlaymiz) |

5. **"Deploy Web Service"** tugmasini bosing. Build tugashini kuting
   (bir necha daqiqa, ffmpeg o'rnatilgani uchun birinchi safar biroz
   uzoqroq davom etishi mumkin).

## 4-qadam: Haqiqiy manzilni yozib, qayta ishga tushirish

1. Deploy tugagach, sahifaning yuqorisida
   `https://objektivka-bot-XXXX.onrender.com` ko'rinishidagi haqiqiy
   manzil chiqadi — uni nusxalang.
2. Chap menyudan **"Environment"** bo'limiga o'ting, `WEBHOOK_HOST`
   qiymatini o'sha haqiqiy manzil bilan almashtiring (oxirida `/` **bo'lmasin**,
   masalan: `https://objektivka-bot-xxxx.onrender.com`).
3. **"Save Changes"** — Render avtomatik qayta deploy qiladi (1-2 daqiqa).
4. Loglarda (Logs bo'limida) `Webhook o'rnatildi: ...` va
   `Webhook server ... portda ishga tushdi` yozuvlarini ko'rsangiz —
   tayyor! Telegramda botga `/start` yozib sinab ko'ring.

## 5-qadam: UptimeRobot bilan botni doim uyg'oq ushlab turish

1. https://uptimerobot.com ga kiring, bepul ro'yxatdan o'ting.
2. **"+ Add New Monitor"**:
   - **Monitor Type**: HTTP(s)
   - **URL**: 3-4-qadamdagi Render manzilingiz (masalan
     `https://objektivka-bot-xxxx.onrender.com`)
   - **Monitoring Interval**: 5 daqiqa
3. Saqlang. Shundan so'ng UptimeRobot har 5 daqiqada shu manzilga
   so'rov yuborib turadi, bot deyarli hech qachon "uxlab qolmaydi".

## Xulosa

Shu bilan bot to'liq **bepul**, karta talab qilmasdan, deyarli 24/7
ishlaydigan holatga keladi — sizga na kompyuterni doim yoniq tutish,
na pul to'lash kerak bo'ladi.
