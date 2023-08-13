from models.cycle_series import CycleSeries
from models.functions import lucas_sequence
from models.time_series import TimeSeries

if __name__ == '__main__':

    generator = TimeSeries(2, 4)
    generator = CycleSeries(lucas_sequence(8,[2,3]))

    for i in range(0):
        time, index, tick = generator.next_tick()
        print(f'{time} , {index}')
