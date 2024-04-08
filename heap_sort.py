from typing import List


def min_heapify(data: List[int]) -> List[int]:

    result = data.copy()

    for i in range(len(result) - 1, -1, -1):
        shift_down(result, i, len(result))

    return result


def shift_down(data: List[int], start: int, stop: int):
    root = start

    while 2 * root + 1 < stop:
        child = 2 * root + 1
        if child + 1 < stop and data[child + 1] < data[child]:
            child += 1
        if data[root] > data[child]:
            data[root], data[child] = data[child], data[root]
            root = child
        else:
            break


def heap_sort(data: List[int]) -> List[int]:
    data = min_heapify(data)
    result = []

    while data:
        result.append(data[0])
        data[0], data[-1] = data[-1], data[0]
        data.pop()
        shift_down(data, 0, len(data))

    return result
