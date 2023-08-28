from models.cycle_series import CycleSeries
from models.functions import lucas_sequence

if __name__ == '__main__':

    no_of_iterations = 10_000_000

    # cycle_length_list = list(range(4, 6))
    cycle_length_list = lucas_sequence(n=1, a=21, b=34)

    # generator = TimeSeries(2, 4)
    generator = CycleSeries(cycle_length_list, rand_seed=122323423, increment_is_netted=True)

    # create freq distribution of all full cycle movements
    # next tick returns standard object including time,index,tick,cycle

    while generator.time < no_of_iterations:
        generator.next_tick()
        # print(f'{generator.time} , {generator.index}, {generator.tick_inc}')

    generator.freq_dist.show_dist()
    generator.show_start_conditions()

    # https://www.hackmath.net/en/calculator/frequency-table
