"""Template configuration utilities."""

import json


def load_template_config(config_path: str = "api/templates.json", fallback: str = "spotify.html.j2") -> str:
    try:
        with open(config_path, "r") as file:
            templates = json.loads(file.read())
            return templates["templates"][templates["current-theme"]]
    except Exception as e:
        print(f"Failed to load templates.\r\n```{e}```")
        return fallback
