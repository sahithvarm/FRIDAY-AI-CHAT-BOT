import speech_recognition as sr


class VoiceListener:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        print("🎧 Calibrating microphone...")

        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

        print("✅ Microphone ready.")

    def listen(self, timeout=None, phrase_time_limit=8):

        with self.microphone as source:

            try:
                print("🎤 Listening...")

                audio = self.recognizer.listen(
                    source,
                    timeout=timeout,
                    phrase_time_limit=phrase_time_limit
                )

                print("🧠 Processing...")

                text = self.recognizer.recognize_google(audio)

                print(f"👤 You: {text}")

                return text.lower().strip()

            except sr.WaitTimeoutError:
                return ""

            except sr.UnknownValueError:
                print("❌ I couldn't understand you.")
                return ""

            except sr.RequestError as error:
                print(f"❌ Speech recognition error: {error}")
                return ""