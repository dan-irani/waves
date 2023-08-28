class FreqDist:

    def __init__(self):
        self.freqDist = {}
        self.count = 0

    def add(self, _key):
        key = str(_key)
        if key in self.freqDist.keys():
            self.freqDist[key] += 1
        else:
            self.freqDist[key] = 1

        self.count += 1

    def get_distribution(self):

        dist_array = []
        fd_sort = dict(reversed(sorted(self.freqDist.items(), key=lambda item: item[1])))

        for key in fd_sort.keys():
            dist_array.append((key, self.freqDist[key] / self.count))

        return dist_array

    def show_dist(self):
        total = 0
        for key, probability in self.get_distribution():
            print(f'{key:>3s} , {probability:>8.6f}')
            total += int(key) * probability

        print(f"Ave: {total}")
