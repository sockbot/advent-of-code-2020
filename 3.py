lines = """

"""

lines = [line for line in lines.split("\n")]


def timer(fn):
    def function_wrapper(x):
        import datetime

        begin_time = datetime.datetime.now()
        fn(x)
        delta_time = datetime.datetime.now() - begin_time
        print(delta_time)

    return function_wrapper


@timer
def part1(lines):
    pass


@timer
def part2(lines):
    pass


print(part1(lines))
print(part2(lines))