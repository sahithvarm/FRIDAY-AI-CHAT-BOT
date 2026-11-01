from pathlib import Path


def create_folder(folder_name: str) -> str:
    """
    Creates a folder on the user's desktop.

    Args:
        folder_name: Name of the folder to create.

    Returns:
        A message describing the result.
    """

    desktop = Path.home() / "Desktop"

    folder = desktop / folder_name

    folder.mkdir(
        parents=True,
        exist_ok=True
    )

    return (
        f"Created the folder "
        f"{folder_name} on your desktop."
    )