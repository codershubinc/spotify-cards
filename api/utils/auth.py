"""Authentication utilities for Spotify API."""

import json
import requests
from base64 import b64encode


def get_auth_header(client_id: str, client_secret: str) -> str:
    """
    Generate Base64-encoded authorization header for Spotify API.
    
    Args:
        client_id: Spotify application client ID
        client_secret: Spotify application client secret
    
    Returns:
        Base64-encoded authorization string
    """
    return b64encode(f"{client_id}:{client_secret}".encode()).decode("ascii")


def refresh_spotify_token(refresh_token: str, client_id: str, client_secret: str, token_url: str) -> str:
    """
    Refresh Spotify access token using refresh token.
    
    Args:
        refresh_token: Spotify refresh token
        client_id: Spotify application client ID
        client_secret: Spotify application client secret
        token_url: Spotify token endpoint URL
    
    Returns:
        New access token
    
    Raises:
        KeyError: If response doesn't contain access_token
    """
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
    }

    headers = {"Authorization": f"Basic {get_auth_header(client_id, client_secret)}"}
    response = requests.post(token_url, data=data, headers=headers).json()

    try:
        return response["access_token"]
    except KeyError:
        print(json.dumps(response))
        print("\n---\n")
        raise KeyError(str(response))
