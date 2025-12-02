"""Utility functions for Spotify widget generation."""

from .auth import get_auth_header, refresh_spotify_token
from .spotify_api import fetch_spotify_data
from .image import load_image_as_base64, generate_color_palette
from .rendering import generate_bar_css, generate_bar_html
from .template import load_template_config

__all__ = [
    'get_auth_header',
    'refresh_spotify_token',
    'fetch_spotify_data',
    'load_image_as_base64',
    'generate_color_palette',
    'generate_bar_css',
    'generate_bar_html',
    'load_template_config',
]
