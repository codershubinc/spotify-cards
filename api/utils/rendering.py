"""SVG rendering utilities for visualizer bars."""

import random


def generate_bar_css(bar_count: int) -> str:
    """
    Generate CSS for animated equalizer bars.
    
    Args:
        bar_count: Number of bars to generate CSS for
    
    Returns:
        CSS string with animation rules for each bar
    """
    bar_css = ""
    left = 1
    for i in range(1, bar_count + 1):
        anim = random.randint(500, 1000)
        # Generate random cubic-bezier values
        x1 = random.random()
        y1 = random.random() * 2
        x2 = random.random()
        y2 = random.random() * 2
        bar_css += (
            f".bar:nth-child({i})  {{ left: {left}px; animation-duration: 15s, {anim}ms; "
            f"animation-timing-function: ease, cubic-bezier({x1},{y1},{x2},{y2}); }}"
        )
        left += 4
    return bar_css


def generate_bar_html(bar_count: int) -> str:
    """
    Generate HTML divs for equalizer bars.
    
    Args:
        bar_count: Number of bar divs to generate
    
    Returns:
        HTML string with bar div elements
    """
    return "".join(["<div class='bar'></div>" for _ in range(bar_count)])
