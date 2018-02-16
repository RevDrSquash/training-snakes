import random
from utils.vector import Vector, up, down, left, right, noop
from base_snake import BaseSnake


class Snake4(BaseSnake):

    def move(self, gamestate):
        options = [up, down, left, right]
        closest_food = gamestate.my_head.closest(gamestate.food)
        if closest_food is not None:
            options = self._directions_to(closest_food, gamestate)

        m = gamestate.first_empty_direction(gamestate.my_head, options, default=noop)
        if m != noop:
            return m

        n = gamestate.neighbouring_heads()
        if len(n) > 0:
            return random.choice(n)

        return m

    def _directions_to(self, goal, gamestate):
        distances = [
            ((goal-gamestate.my_head-left).magnitude, left),
            ((goal-gamestate.my_head-right).magnitude, right),
            ((goal-gamestate.my_head-up).magnitude, up),
            ((goal-gamestate.my_head-down).magnitude, down),
        ]
        distances.sort(key=lambda x: x[0], reverse=False)
        return [d[1] for d in distances]

    def name(self):
        return "Training Snake 4"

    def color(self):
        return "#05f299"

    def head_url(self):
        return ""

    def taunt(self):
        return ""

    def end(self):
        pass
