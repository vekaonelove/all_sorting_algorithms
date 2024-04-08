from typing import List


def radix_sort(array: List[str], k: int) -> List[int]:
    array = [([int(c) for c in e], i) for i, e in enumerate(array)]
    for i in range(k):
        array.sort(key=lambda x: x[0][-i - 1])

    return [e[1] for e in sorted((e[1], i) for i, e in enumerate(array))]
