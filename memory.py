import json
from pathlib import Path


class Memory:

    def __init__(self):

        self.memory_folder = (
            Path(__file__).parent.parent / "memory"
        )

        self.memory_folder.mkdir(
            exist_ok=True
        )

        self.memory_file = (
            self.memory_folder / "conversation.json"
        )

        if not self.memory_file.exists():

            self.memory_file.write_text(
                "[]",
                encoding="utf-8"
            )

    def load(self):

        try:

            with open(
                self.memory_file,
                "r",
                encoding="utf-8"
            ) as file:

                return json.load(file)

        except (
            json.JSONDecodeError,
            FileNotFoundError
        ):

            return []

    def save(self, history):

        with open(
            self.memory_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                history,
                file,
                indent=4,
                ensure_ascii=False
            )

    def add_user_message(self, message):

        history = self.load()

        history.append({
            "role": "user",
            "content": message
        })

        self.save(history)

    def add_assistant_message(self, message):

        history = self.load()

        history.append({
            "role": "assistant",
            "content": message
        })

        self.save(history)

    def clear(self):

        self.save([])

    def get_history(self):

        return self.load()