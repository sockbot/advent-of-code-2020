def part2(numbers):
    for i in numbers:
        for j in numbers:
            for k in numbers:
                if i + j + k == 2020:
                    return i * j * k


with open("1a.txt", "r") as file:
    numbers = [int(number.strip()) for number in file.readlines()]
    print(part2(numbers))
