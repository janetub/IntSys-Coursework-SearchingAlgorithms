import pygame
from pgu import gui

class GUI:
    def __init__(self, graph):
        self.graph = graph
        self.form = gui.Form()
        self.container = gui.Container(align=-1, valign=-1)
        self.form.add(self.container, 0, 0)

        self.button = gui.Button("Add Node")
        self.button.connect(gui.CLICK, self.add_node)
        self.container.add(self.button, 10, 10)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.graph.add_node(event.pos)

    def draw(self, screen):
        self.graph.draw(screen)
        self.container.paint(screen)
