@echo off
REM Bu skript botni doimiy ishlab turishini ta'minlaydi.
REM Agar bot biror xatolik bilan to'xtab qolsa, 5 soniyadan keyin
REM avtomatik qayta ishga tushadi.

cd /d "%~dp0"

:LOOP
echo [%date% %time%] Bot ishga tushmoqda...
call venv\Scripts\activate.bat
python bot.py
echo [%date% %time%] Bot to'xtadi. 5 soniyadan keyin qayta ishga tushadi...
timeout /t 5 /nobreak > nul
goto LOOP
