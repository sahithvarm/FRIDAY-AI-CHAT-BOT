import speech_recognition as sr


class VoiceListener:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        with self.microphone as source:
            print("🎧 Calibrating microphone...")
            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

        print("✅ Microphone ready.")

    def listen(self, timeout=None, phrase_time_limit=8):

        with self.microphone as source:

            try:
                audio = self.recognizer.listen(
                    source,
                    timeout=timeout,
                    phrase_time_limit=phrase_time_limit
                )

                print("🧠 Processing speech...")

                text = self.recognizer.recognize_google(audio)

                return text.lower().strip()

            except sr.WaitTimeoutError:
                return ""

            except sr.UnknownValueError:
                print("❌ Couldn't understand.")
                return ""

            except sr.RequestError as error:
                print(f"❌ Speech recognition error: {error}")
                return ""