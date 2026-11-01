import webbrowser
from urllib.parse import quote


def open_website(url: str) -> str:
    """
    Opens a website in the user's default web browser.

    Args:
        url: Website URL such as youtube.com or google.com.

    Returns:
        A message describing the result.
    """

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    webbrowser.open(url)

    return f"Opened {url} successfully."


def search_web(query: str) -> str:
    """
    Searches Google for information.

    Args:
        query: The search query.

    Returns:
        A message describing the search.
    """

    url = (
        "https://www.google.com/search?q="
        + quote(query)
    )

    webbrowser.open(url)

    return f"Searched Google for {query}."


def search_youtube(query: str) -> str:
    """
    Searches YouTube for videos.

    Args:
        query: The YouTube search query.

    Returns:
        A message describing the search.
    """

    url = (
        "https://www.youtube.com/results?search_query="
        + quote(query)
    )

    webbrowser.open(url)

    return f"Searched YouTube for {query}."