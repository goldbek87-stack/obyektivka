"""
Telegram ovozli xabarni (.ogg/opus) matnga aylantirish.

Talab qiladi:
  - ffmpeg tizimda o'rnatilgan bo'lishi kerak (pydub shu orqali konvertatsiya qiladi)
  - internet aloqasi (Google Web Speech API bepul, lekin internetga bog'liq)
"""
import os
import uuid
import logging

from pydub import AudioSegment
import speech_recognition as sr

from config import STT_LANGUAGES, TMP_DIR

logger = logging.getLogger(__name__)

recognizer = sr.Recognizer()


def _ogg_to_wav(ogg_path: str) -> str:
    wav_path = os.path.join(TMP_DIR, f"{uuid.uuid4().hex}.wav")
    audio = AudioSegment.from_file(ogg_path)
    audio = audio.set_frame_rate(16000).set_channels(1)
    audio.export(wav_path, format="wav")
    return wav_path


def transcribe_ogg(ogg_path: str) -> str | None:
    """
    .ogg ovoz faylini matnga aylantiradi.
    Muvaffaqiyatli bo'lsa matnni, aks holda None qaytaradi.
    """
    wav_path = None
    try:
        wav_path = _ogg_to_wav(ogg_path)
        with sr.AudioFile(wav_path) as source:
            audio_data = recognizer.record(source)

        last_error = None
        for lang in STT_LANGUAGES:
            try:
                text = recognizer.recognize_google(audio_data, language=lang)
                if text and text.strip():
                    logger.info("STT success (%s): %s", lang, text)
                    return text.strip()
            except sr.UnknownValueError as e:
                last_error = e
                continue
            except sr.RequestError as e:
                last_error = e
                logger.warning("STT request error (%s): %s", lang, e)
                continue

        logger.warning("STT failed for all languages: %s", last_error)
        return None
    except Exception:
        logger.exception("Ovozni matnga aylantirishda xatolik")
        return None
    finally:
        for p in (ogg_path, wav_path):
            if p and os.path.exists(p):
                try:
                    os.remove(p)
                except OSError:
                    pass
