"""Implements a Press Any Key to Exit Scene"""

import pygame
from .scene import Scene

class PressAnyKeyToExitScene(Scene):
    """Empty scene where it will invalidate when a key is pressed."""

    def process_event(self, event):
        """Process game events."""
        super().process_event(event)

        if event.type == pygame.KEYDOWN or event.type == pygame.JOYBUTTONDOWN:
            self._is_valid = False
