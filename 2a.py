with open("2.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    validPasswordCount = 0
    for line in lines:
        rule = line.split(": ")[0]
        password = line.split(": ")[1]
        countRange = rule.split(" ")[0]
        charMin = int(countRange.split("-")[0])
        charMax = int(countRange.split("-")[1])
        char = rule.split(" ")[1]
        charCount = password.count(char)
        if charCount >= charMin and charCount <= charMax:
            validPasswordCount += 1
    print(validPasswordCount)

with open("2.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    validPasswordCount = 0
    for line in lines:
        rule = line.split(": ")[0]
        password = line.split(": ")[1]
        countRange = rule.split(" ")[0]
        charMin = int(countRange.split("-")[0])
        charMax = int(countRange.split("-")[1])
        char = rule.split(" ")[1]
        if (password[charMin - 1] == char and password[charMax - 1] != char) or (
            password[charMin - 1] != char and password[charMax - 1] == char
        ):
            validPasswordCount += 1
    print(validPasswordCount)
