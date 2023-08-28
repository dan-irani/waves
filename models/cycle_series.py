import random
import sys

from models.cycle import Cycle
from models.freqdist import FreqDist


class CycleSeries:

    def __init__(self, cycle_length_list, rand_seed=None, increment_is_netted=True):

        self.cycle_object_list = []  # list of cycle objects
        self.cycle_count = len(cycle_length_list)
        self.increment_is_netted = increment_is_netted
        self.freq_dist = FreqDist()

        if rand_seed is not None:
            # use the supplied random seed instead of a random one
            self.seed_value = int(rand_seed)
        else:
            self.seed_value = random.randint(0, sys.maxsize)

        random.seed(self.seed_value)

        self.index = 0
        self.time = 0
        self.cycle_index = 0
        self.tick_inc = 0

        for length in cycle_length_list:
            # cycle phase is currently random between 1 and (2 * cycle length)
            cycle_phase = random.randint(a=1, b=2 * length)
            # cycle_phase = 1
            self.cycle_object_list.append(Cycle(length, cycle_phase))

    def show_start_conditions(self):

        start_conditions = ''

        for c in self.cycle_object_list:
            if len(start_conditions):
                start_conditions += ' & '
            start_conditions += f'{{{c.length}:{c.phase_initial}}}'

        print(f'cycles = [ {start_conditions} ]')

    def next_tick(self):

        self.tick_inc = 0

        if self.increment_is_netted:
            for c in range(0, self.cycle_count):
                self.tick_inc += self.cycle_object_list[c].next_tick()
                self.cycle_index = (self.cycle_index % self.cycle_count) + 1
                self.time += 1
        else:
            self.tick_inc = self.cycle_object_list[self.cycle_index - 1].next_tick()
            self.cycle_index = (self.cycle_index % self.cycle_count) + 1
            self.time += 1

        self.index += self.tick_inc
        self.freq_dist.add(self.index)
