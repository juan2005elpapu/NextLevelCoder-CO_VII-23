import random
from dino_runner.components.obstacles.obsacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    def __init__(self):
        self.image =BIRD[0]
        super().__init__(self.image)
        self.rect.y = random.randint(50,320)
        self.counter = 0

    def update(self, game_speed):
        self.counter += 1
        self.image = BIRD[0] if self.counter % 5 == 0 else BIRD[1]
        return super().update(game_speed)
    