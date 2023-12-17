import pygame
from gui import GUI
from graph import Graph

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    graph = Graph()
    gui = GUI(graph)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            gui.handle_event(event)

        screen.fill((0, 0, 0))
        gui.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
