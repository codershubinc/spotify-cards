"""Template configuration utilities."""

import json


def load_template_config(config_path: str = "api/templates.json", fallback: str = "spotify.html.j2") -> str:
    """
    Load the current template name from configuration file.

    Args:
        config_path: Path to the templates configuration JSON file
        fallback: Fallback template name if config loading fails

    Returns:
        Template filename to use for rendering
    """
    try:
        with open(config_path, "r") as file:
            templates = json.loads(file.read())
            return templates["templates"][templates["current-theme"]]
    except Exception as e:
        print(f"Failed to load templates.\r\n```{e}```")
        return fallback
