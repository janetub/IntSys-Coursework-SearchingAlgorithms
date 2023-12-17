import pygame
import networkx as nx

class Graph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, pos):
        self.graph.add_node(len(self.graph.nodes), pos=pos)

    def draw(self, screen):
        for node, pos in self.graph.nodes.data('pos'):
            pygame.draw.circle(screen, (255, 255, 255), pos, 10)
