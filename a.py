#! /usr/bin/python3

import sys

rooms_len = None
row_len = None
rooms_weights = None


def find_solution(k, closed_rooms):
    global rooms_len
    global row_len
    global rooms_weights

    if k == 0:
        amount = 0
        for i in range(rooms_len):
            for j in range(row_len):
                if not closed_rooms[i][j]:
                    amount += rooms_weights[i][j]
        return amount

    max_value = 0
    for i in range(rooms_len):
        if any(closed_rooms[i]):
            continue
        for j in range(row_len):
            if not closed_rooms[i][j]:
                if i - 1 >= 0 and closed_rooms[i - 1][(j + 1) % 2]:
                    continue
                if i + 1 < len(closed_rooms) and closed_rooms[i + 1][(j + 1) % 2]:
                    continue

                new_closed_rooms = [[closed_rooms[i][j] for j in range(row_len)] for i in range(rooms_len)]
                new_closed_rooms[i][j] = True
                value = find_solution(k - 1, new_closed_rooms)
                if value > max_value:
                    max_value = value
    return max_value


def read_input(input_source):
    rooms = []

    n_and_k = input_source.readline().split()
    N = int(n_and_k[0])
    k = int(n_and_k[1])

    if N == 0 and k == 0:
        return N, k, rooms

    for row in range(N):
        two_rooms = list(map(lambda i: int(i), input_source.readline().split()))
        rooms.append(two_rooms)

    return N, k, rooms


f = open("Problem A/sample3.in", "r")  # Time Limit Exceeded

while True:
    N, k, rooms = read_input(f)
    # N, k, rooms = read_input(sys.stdin)
    if N == 0 and k == 0:
        break

    rooms_len = len(rooms)
    row_len = len(rooms[0]) if rooms_len > 0 else 0
    rooms_weights = rooms
    closed_rooms = [[False, False] for i in range(len(rooms))]

    print(find_solution(k, closed_rooms))

f.close()
