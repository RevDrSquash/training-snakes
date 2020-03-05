from snakes.base_snake import BaseSnake
from snakes.snake_4 import ScaredSnake
from snakes.snake_5 import SimpleHungrySnake


class SimpleSometimesHungrySnake(BaseSnake):
    DIFFICULTY = 6
    HUNGER_THRESHOLD = 30

    def move(self, gamestate):
        if gamestate.me.health < self.THRESHOLD:
            return ScaredSnake().move(gamestate)
        return SimpleHungrySnake().move(gamestate)

    def name(self):
        return "Training Snake 6"

    def color(self):
        return "#05f299"

    def head_url(self):
        return ""

    def taunt(self):
        return ""

    def end(self, details):
        pass
