from commands.basic import handle_basic_command
from commands.browser import handle_browser_command
from commands.system import handle_system_command


class Assistant:

    def process(self, command):

        response = handle_basic_command(command)

        if response:
            return response

        response = handle_browser_command(command)

        if response:
            return response

        response = handle_system_command(command)

        if response:
            return response

        return (
            "I understood your command, "
            "but I don't know how to perform it yet."
        )