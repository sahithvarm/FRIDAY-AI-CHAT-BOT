from core.listener import VoiceListener
from core.speaker import Speaker
from core.brain import FridayBrain


def main():

    listener = VoiceListener()
    speaker = Speaker()
    brain = FridayBrain()

    speaker.speak(
        "Friday is online and ready."
    )

    while True:

        print("\n🎤 Listening...")

        command = listener.listen(
            timeout=None,
            phrase_time_limit=15
        )

        if not command:
            continue

        print(f"👤 You: {command}")

        exit_commands = [
            "exit",
            "quit",
            "shutdown friday",
            "exit friday",
            "goodbye friday",
            "stop listening"
        ]

        if any(
            phrase in command
            for phrase in exit_commands
        ):

            speaker.speak(
                "Goodbye. I'll be here when you need me."
            )

            break

        try:

            answer = brain.ask(command)

            if answer:
                speaker.speak(answer)

        except Exception as error:

            print(
                f"\n❌ AI Error: {error}"
            )

            speaker.speak(
                "Sorry, I couldn't process that request."
            )


if __name__ == "__main__":
    main()