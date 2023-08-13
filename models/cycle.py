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