import asyncio
import os
import re
import tempfile

import edge_tts
import pygame


class Speaker:

    def __init__(self):

        self.english_voice = "en-IN-PrabhatNeural"
        self.telugu_voice = "te-IN-MohanNeural"

        pygame.mixer.init()

    def speak(self, text, language="auto"):

        print(f"🤖 Friday: {text}")

        detected_language = self.detect_language(
            text,
            language
        )

        if detected_language == "telugu":
            voice = self.telugu_voice
        else:
            voice = self.english_voice

        print(f"🔊 Voice: {voice}")

        try:

            asyncio.run(
                self._generate_and_play(
                    text,
                    voice
                )
            )

        except Exception as error:

            print(f"❌ Voice Error: {error}")

    def detect_language(self, text, language):

        if language in ["english", "telugu"]:
            return language

        # Telugu Unicode range:
        # 0C00 - 0C7F

        telugu_characters = re.findall(
            r"[\u0C00-\u0C7F]",
            text
        )

        if len(telugu_characters) > 0:
            return "telugu"

        return "english"

    async def _generate_and_play(
        self,
        text,
        voice
    ):

        communicate = edge_tts.Communicate(
            text,
            voice,
            rate="-5%",
            volume="+0%",
            pitch="+0Hz"
        )

        with tempfile.NamedTemporaryFile(
            suffix=".mp3",
            delete=False
        ) as audio_file:

            audio_path = audio_file.name

        try:

            await communicate.save(
                audio_path
            )

            pygame.mixer.music.load(
                audio_path
            )

            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():

                await asyncio.sleep(0.1)

        finally:

            pygame.mixer.music.stop()

            try:
                os.remove(audio_path)

            except PermissionError:
                pass