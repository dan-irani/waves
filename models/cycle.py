class Cycle:
    def __init__(self, _length, _phase_initial):
        self.length = _length
        self.phase_max = 2 * _length
        self.phase_initial = _phase_initial

        # ensure initial phase is between 1 and (2 * cycle length)
        if not 1 <= self.phase_initial <= self.phase_max:
            self.phase_initial = (self.phase_initial % self.phase_max)

        # adjust start phase to be one phase earlier
        # so the first tick is correct after increment

        self.phase_current = self.phase_initial - 1

    def next_tick(self):
        # return +1 if phase is between 1 and length
        # return -1 if phase is between (length + 1) and (2 * length)
        self.phase_current = (self.phase_current % self.phase_max) + 1
        return 1 if self.phase_current <= self.length else -1
