import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird


class ObstacleManager:

    def __init__(self):
        self.has_obstacle = False
        self.obstacle = None

    def update(self, game):
        if not self.has_obstacle:
            self.create_obstacle()
        self.has_obstacle = self.obstacle.update(game.game_speed)
        if game.player.rect.colliderect(self.obstacle.rect):
            pygame.time.delay(300)
            game.playing = False
    
    def create_obstacle(self):
        obstacle_list = [Cactus(),Bird()]
        self.obstacle = random.choice(obstacle_list)
        self.has_obstacle = True

    def draw(self,screen):
        if self.has_obstacle:
            self.obstacle.draw(screen)
        