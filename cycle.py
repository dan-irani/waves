import random
import sys


class Cycle:
    def __init__(self, _cycle_size, _cycle_phase):
        self.cycle_size = _cycle_size
        self.max_phase = 2 * _cycle_size

        # now adjust start phase to be one phase earlier
        # so the first tick is correct after increment

        self.start_phase = _cycle_phase - 1

        if not 1 <= self.start_phase <= self.max_phase:
            self.start_phase = 10

        self.phase = self.start_phase

    def next_tick(self):
        self.phase = (self.phase % self.max_phase) + 1
        return 1 if self.phase <= self.cycle_size else -1


class Generator():
    def __init__(self, _cycle_count, _rand_seed=None):
        self.cycle_count = _cycle_count

        if _rand_seed is not None:
            # use the supplied random seed instead of a random one
            self.seed_value = int(_rand_seed)
        else:
            self.seed_value = random.randint(0, sys.maxsize)

        random.seed(self.seed_value)

        self.index = 0
        self.time = 0
        self.cycle_index = 0

        self.cycle_list = []

        self.fib_list = self.fibonacci(self.cycle_count)
        print(self.fib_list)

        for cycle_size in self.fib_list:
            cycle_phase = random.randint(1, 2 * cycle_size)
            self.cycle_list.append(Cycle(cycle_size, cycle_phase))

    def next_tick(self):
        tick_inc = self.cycle_list[self.cycle_index - 1].next_tick()
        self.index += tick_inc
        self.time += 1

        self.cycle_index = (self.cycle_index % self.cycle_count) + 1
        return self.time, self.index, tick_inc

    @staticmethod
    def fibonacci(n):
        # any lucas starting pair
        fib_list = [7, 11]
        if n > 2:
            for f in range(n - 2):
                fib_list.append(fib_list[f] + fib_list[f + 1])

        return fib_list
