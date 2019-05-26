#! /usr/bin/python3

import sys

rooms_len = None
row_len = None
rooms_weights = None


def two2one(row, col):
    global row_len
    return row_len * row + col


def get_bit(i, pos):
    return i >> pos & 1


def set_bit(i, pos):
    return i | (1 << pos)


def find_solution(k, closed_rooms):
    global rooms_len
    global row_len
    global rooms_weights

    if k == 0:
        amount = 0
        for i in range(rooms_len):
            for j in range(row_len):
                if get_bit(closed_rooms, two2one(i, j)) == 0:
                    amount += rooms_weights[i][j]
        return amount

    max_value = 0
    for i in range(rooms_len):
        if any([get_bit(closed_rooms, two2one(i, j)) for j in range(row_len)]):
            continue
        for j in range(row_len):
            if get_bit(closed_rooms, two2one(i, j)) == 0:
                if i - 1 >= 0 and get_bit(closed_rooms, two2one(i - 1, (j + 1) % 2)) == 1:
                    continue
                if i + 1 < rooms_len and get_bit(closed_rooms, two2one(i + 1, (j + 1) % 2)) == 1:
                    continue

                new_closed_rooms = set_bit(closed_rooms, two2one(i, j))
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

    print(find_solution(k, 0))

f.close()
