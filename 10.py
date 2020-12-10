lines = """99
151
61
134
112
70
75
41
119
137
158
50
167
60
116
117
62
82
31
3
72
88
165
34
8
14
27
108
166
71
51
42
135
122
140
109
1
101
2
77
85
76
143
100
127
7
107
13
148
118
56
159
133
21
154
152
130
78
54
104
160
153
95
49
19
69
142
63
11
12
29
98
84
28
17
146
161
115
4
94
24
126
136
91
57
30
155
79
66
141
48
125
162
37
40
147
18
20
45
55
83
"""
# lines = """16
# 10
# 15
# 5
# 1
# 11
# 7
# 19
# 6
# 12
# 4"""
# lines = """28
# 33
# 18
# 42
# 31
# 14
# 46
# 20
# 48
# 47
# 24
# 23
# 49
# 45
# 19
# 38
# 39
# 11
# 1
# 32
# 25
# 35
# 8
# 17
# 7
# 9
# 4
# 2
# 34
# 10
# 3"""
lines = lines.strip()
lines = [int(line) for line in lines.split("\n")]


from helpers import timer


# @timer
def part1():
    adapters = set(lines)
    rating = 0
    oneJoltDiff = 0
    twoJoltDiff = 0
    threeJoltDiff = 0
    totalJolts = 0
    while len(adapters) > 0:
        if rating + 1 in adapters:
            adapters.discard(rating + 1)
            oneJoltDiff += 1
            rating += 1
        elif rating + 2 in adapters:
            adapters.discard(rating + 2)
            twoJoltDiff += 1
            rating += 2
        elif rating + 3 in adapters:
            adapters.discard(rating + 3)
            threeJoltDiff += 1
            rating += 3
        totalJolts += rating
    totalJolts += 3
    threeJoltDiff += 1
    return oneJoltDiff * threeJoltDiff


seen = {}


def howManyWays(adapters, start, end):
    if start == end:
        return 1
    if start not in adapters:
        return 0
    if start in seen:
        return seen[start]
    answer = 0
    for i in [start + 1, start + 2, start + 3]:
        answer += howManyWays(adapters, i, end)
    seen[start] = answer
    return answer


import copy

# @timer
def part2():
    adapters = copy.copy(lines)
    adapters.append(max(adapters) + 3)
    adapters.append(0)
    adapters.sort()
    return howManyWays(adapters, min(adapters), max(adapters) + 3)


print(f"Answer 1: {part1()}")
print(f"Answer 2: {part2()}")
