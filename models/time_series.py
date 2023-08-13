import random
import sys


class TimeSeries:

    def __init__(self, prob_a, prob_b, rand_seed=None):

        self.pool_size = 1_000_000
        self.index = 0
        self.time = 0

        if rand_seed is not None:
            # use the supplied random seed instead of a random one
            self.seed_value = int(rand_seed)
        else:
            self.seed_value = random.randint(0, sys.maxsize)

        random.seed(self.seed_value)

        self.polarity = True if random.randint(0, 1) == 1 else False
        self.pool_boundary = self.pool_size - self.pool_size * prob_a / prob_b

    def next_tick(self) -> (int, int):
        if random.randint(0, self.pool_size) >= self.pool_boundary:
            self.polarity = not self.polarity

        tick_inc = 1 if self.polarity else -1

        self.index += tick_inc
        self.time += 1

        return self.time, self.index, tick_inc
