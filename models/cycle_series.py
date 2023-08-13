import random
import sys

from models.cycle import Cycle
from models.functions import lucas_sequence


class CycleSeries:

    def __init__(self, cycle_list, rand_seed=None):

        self.cycle_list = cycle_list
        self.cycle_count = len(self.cycle_list)
        self.cycle_object_list = []

        if rand_seed is not None:
            # use the supplied random seed instead of a random one
            self.seed_value = int(rand_seed)
        else:
            self.seed_value = random.randint(0, sys.maxsize)

        random.seed(self.seed_value)

        self.index = 0
        self.time = 0
        self.cycle_index = 0

        for cycle_size in self.cycle_list:
            cycle_phase = random.randint(1, 2 * cycle_size)
            print(cycle_size,cycle_phase)
            self.cycle_object_list.append(Cycle(cycle_size, cycle_phase))

    def next_tick(self):
        tick_inc = self.cycle_object_list[self.cycle_index - 1].next_tick()
        self.index += tick_inc
        self.time += 1

        self.cycle_index = (self.cycle_index % self.cycle_count) + 1
        return self.time, self.index, tick_inc

