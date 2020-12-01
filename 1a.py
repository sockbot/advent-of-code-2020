def part1(numbers):
    for i in numbers:
        for j in numbers:
            if i + j == 2020:
                return i * j


with open("1a.txt", "r") as file:
    numbers = [int(number.strip()) for number in file.readlines()]
    print(part1(numbers))
