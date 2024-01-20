import pygame

from .actor import Actor

class EventActor(Actor):
    """An actor that can be manipulated by Events"""

    def process_event(self, event):
        raise NotImplementedError
