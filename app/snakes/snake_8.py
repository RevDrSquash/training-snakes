import random
from base_snake import BaseSnake
from snake_3 import Snake3

class Snake8(BaseSnake):

    THRESHOLD = 30

    def move(self, gamestate):

        if len(gamestate.possible_kill_coords) > 0:
            goal = random.choice(gamestate.possible_kill_coords)
            return goal - gamestate.me.head

        if gamestate.me.health > self.THRESHOLD:
            return Snake3().move(gamestate)

        visitable_tails = gamestate.distance_to(gamestate.me.head, gamestate.all_tails)
        if len(visitable_tails) == 0:
            return Snake3().move(gamestate)

        closest_tail = visitable_tails[0]
        return gamestate.move_towards(closest_tail)

    def name(self):
        return "Training Snake 8"

    def color(self):
        return "#05f299"

    def head_url(self):
        return ""

    def taunt(self):
        return ""

    def end(self):
        pass