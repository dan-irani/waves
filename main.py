from models.cycle_series import CycleSeries
from models.functions import lucas_sequence

if __name__ == '__main__':

    no_of_iterations = 1_000_000

    # generator = TimeSeries(2, 4)

    # cycle_length_list = lucas_sequence(n=4, a=21, b=34)
    cycle_length_list = [21, 34]
    cycle_phase_list = [1,1]

    generator = CycleSeries(cycle_length_list, cycle_phase_list, increment_is_netted=True)

    # create freq distribution of all full cycle movements
    # next tick returns standard object including time,index,tick,cycle

    while generator.time < no_of_iterations:
        generator.next_tick()
        # print(f'{generator.time} , {generator.index}, {generator.tick_inc}')

    generator.freq_dist.show_dist()
    generator.show_start_conditions()
