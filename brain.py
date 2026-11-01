import os

from google import genai

from core.memory import Memory

from tools.browser import (
    open_website,
    search_web,
    search_youtube
)

from tools.system import (
    open_application
)

from tools.files import (
    create_folder
)


class FridayBrain:

    def __init__(self):

        # -----------------------------
        # API KEY
        # -----------------------------

        api_key = os.getenv(
            "GEMINI_API_KEY"
        )

        if not api_key:

            raise RuntimeError(
                "GEMINI_API_KEY is not set."
            )

        # -----------------------------
        # Gemini
        # -----------------------------

        self.client = genai.Client(
            api_key=api_key
        )

        self.model = "gemini-3.5-flash-lite"

        # -----------------------------
        # Memory
        # -----------------------------

        self.memory = Memory()

        # -----------------------------
        # Friday personality
        # -----------------------------

        self.system_prompt = """
You are Friday, a helpful personal AI assistant.

You are running on the user's Windows computer.

Your responses will be spoken aloud.

Rules:

- Understand natural language.
- Be conversational.
- Keep answers concise.
- Use tools when the user requests an action.
- Never claim an action happened unless the tool actually completed it.
- Remember relevant conversation context.
- Do not invent memories.
"""

        # -----------------------------
        # Tools
        # -----------------------------

        self.tools = [
            open_website,
            search_web,
            search_youtube,
            open_application,
            create_folder
        ]

    def ask(self, user_message):

        # Load previous conversation
        history = self.memory.get_history()

        # Convert stored history
        # into Gemini conversation format

        contents = []

        for message in history:

            role = message["role"]

            if role == "assistant":
                role = "model"

            contents.append({
                "role": role,
                "parts": [
                    {
                        "text": message["content"]
                    }
                ]
            })

        # Add current message

        contents.append({
            "role": "user",
            "parts": [
                {
                    "text": user_message
                }
            ]
        })

        # Ask Gemini

        response = self.client.models.generate_content(

            model=self.model,

            contents=contents,

            config={
                "system_instruction":
                    self.system_prompt,

                "tools": self.tools
            }
        )

        answer = response.text

        # Save conversation

        self.memory.add_user_message(
            user_message
        )

        self.memory.add_assistant_message(
            answer
        )

        return answer