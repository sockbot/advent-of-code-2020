lines = """
"""
lines = lines.strip()
lines = [line for line in lines.split("\n")]


def timer(fn):
    def function_wrapper(x):
        import datetime

        begin_time = datetime.datetime.now()
        result = fn(x)
        delta_time = datetime.datetime.now() - begin_time
        print(delta_time)
        return result

    return function_wrapper


@timer
def part1(lines):
    return


@timer
def part2(lines):
    return


print(f"Answer 1: {part1(lines)}")
print(f"Answer 2: {part2(lines)}")
