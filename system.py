import subprocess


def open_application(application: str) -> str:
    """
    Opens an allowed Windows application.

    Args:
        application: Application name such as notepad,
        calculator, or paint.

    Returns:
        A message describing the result.
    """

    allowed_apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe",
    }

    application = application.lower().strip()

    if application not in allowed_apps:
        return (
            f"I cannot open {application}. "
            "That application is not currently allowed."
        )

    subprocess.Popen(
        allowed_apps[application]
    )

    return f"Opened {application} successfully."