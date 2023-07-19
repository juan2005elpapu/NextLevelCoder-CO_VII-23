import random
from dino_runner.components.obstacles.obsacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS


class Cactus(Obstacle):
    def __init__(self):
        image_list = SMALL_CACTUS + LARGE_CACTUS
        selected_image = random.choice(image_list)
        super().__init__(selected_image)
        if selected_image == image_list[0] or selected_image == image_list[1] or selected_image == image_list[2] :
            self.rect.y = 320
        else:
            self.rect.y = 300