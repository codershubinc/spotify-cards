"""Image processing and color palette generation utilities."""

from io import BytesIO
from base64 import b64encode, b64decode
from urllib.parse import urlparse
from typing import List, Tuple, Union

import requests
from colorthief import ColorThief  # type: ignore


def load_image_as_base64(url: str) -> str:
    """
    Fetch an image from a URL and return it as base64-encoded string.

    Args:
        url: Image URL to fetch

    Returns:
        Base64-encoded image data
    """
    response = requests.get(url)
    return b64encode(response.content).decode("ascii")


def generate_color_palette(album_art: Union[str, bytes, bytearray, None],
                           color_count: int,
                           placeholder_image: str) -> List[Tuple[int, int, int]]:
    """
    Generate a color palette from an album image using ColorThief.

    Args:
        album_art: Can be a URL string, raw bytes, or None
        color_count: Number of colors to extract from the image
        placeholder_image: Base64-encoded placeholder image to use as fallback

    Returns:
        List of RGB tuples representing the color palette

    Notes:
        - If album_art is bytes/bytearray, uses them directly
        - If album_art is a string URL from Spotify/scdn domains, fetches the image
        - Otherwise (None or non-Spotify URL), uses the placeholder image
    """
    if isinstance(album_art, (bytes, bytearray)):
        img_bytes = album_art
    elif isinstance(album_art, str) and album_art:
        # Only fetch album art images if hosted by Spotify to prevent external API calls
        domain = urlparse(album_art).netloc.lower()
        if any(k in domain for k in ("spotify", "scdn")):
            img_bytes = requests.get(album_art).content
        else:
            # Avoid fetching unknown 3rd-party images
            img_bytes = b64decode(placeholder_image)
    else:
        # Fallback to built-in placeholder image
        img_bytes = b64decode(placeholder_image)

    colorthief = ColorThief(BytesIO(img_bytes))
    palette = colorthief.get_palette(color_count)  # type: ignore
    return palette
