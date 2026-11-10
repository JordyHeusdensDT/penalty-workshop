import random

TARGETS = ["left-low", "left-high", "center-low", "center-high", "right-low", "right-high"]


def shoot(state):
    return random.choice(TARGETS), round(random.uniform(0.3, 1.0), 2)


def keep(state):
    return random.choice(["left", "center", "right"])
