"""Spotify API data fetching utilities."""

from typing import Dict, Any
import requests


def fetch_spotify_data(url: str, access_token: str) -> Dict[str, Any]:
    """
    Fetch data from Spotify API endpoint.

    Args:
        url: Spotify API endpoint URL
        access_token: Valid Spotify access token

    Returns:
        JSON response from Spotify API

    Raises:
        Exception: If API returns 204 (no data) or other errors
    """
    response = requests.get(
        url, headers={"Authorization": f"Bearer {access_token}"}
    )

    if response.status_code == 401:
        raise Exception(f"401 Unauthorized - Token may be expired")
    elif response.status_code == 204 or not response.content:
        raise Exception(f"{url} returned no data.")
    elif response.status_code != 200:
        raise Exception(
            f"{url} returned HTTP {response.status_code}: {response.text[:200]}"
        )
    else:
        return response.json()
