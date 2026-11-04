import random

def gen_random(count, low, high):
    for _ in range(count):
        yield random.randint(low, high)
