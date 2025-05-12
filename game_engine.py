"""
Простой 2D-игровой движок.
"""

import pygame
import sys
from typing import Tuple


class GameObject:
    """
    Базовый класс игрового объекта.
    """

    def __init__(self, x: int, y: int, width: int, height: int, color: Tuple[int, int, int]):
        """
        Инициализация объекта.
        
        Args:
            x (int): Позиция X.
            y (int): Позиция Y.
            width (int): Ширина.
            height (int): Высота.
            color (Tuple): Цвет (R, G, B).
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, screen) -> None:
        """
        Отрисовывает объект.
        
        Args:
            screen: Экран Pygame.
        """
        pygame.draw.rect(screen, self.color, self.rect)


class GameEngine:
    """
    Основной цикл игры.
    """

    def __init__(self, width: int = 800, height: int = 600, title: str = "Game"):
        """
        Инициализация движка.
        
        Args:
            width (int): Ширина окна.
            height (int): Высота окна.
            title (str): Заголовок окна.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.objects = []

    def add_object(self, obj: GameObject) -> None:
        """
        Добавляет объект в игру.
        
        Args:
            obj (GameObject): Игровой объект.
        """
        self.objects.append(obj)

    def run(self) -> None:
        """
        Запускает игровой цикл.
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.screen.fill((0, 0, 0))
            for obj in self.objects:
                obj.draw(self.screen)
            
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    engine = GameEngine()
    player = GameObject(100, 100, 50, 50, (255, 0, 0))
    engine.add_object(player)
    engine.run()