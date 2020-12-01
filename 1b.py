import datetime


def part2(numbers):
    numbers.sort()
    for i in numbers:
        for j in numbers:
            for k in numbers:
                if i + j + k == 2020:
                    return i * j * k


with open("1a.txt", "r") as file:
    numbers = [int(number.strip()) for number in file.readlines()]
    begin_time = datetime.datetime.now()
    answer = part2(numbers)
    end_time = datetime.datetime.now() - begin_time
    print(end_time)
    print(answer)
