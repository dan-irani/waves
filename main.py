from cycle import Generator

if __name__ == '__main__':
    fib_count = 9

    g = Generator(fib_count)

    for i in range(10000):
        time, index, tick = g.next_tick()
        print(f'{time} , {index}')


