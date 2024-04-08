from typing import List, Tuple


def merge_sorted_subarrays(data: List[int], left_index: int, middle_index: int, right_index: int):
    left = data[left_index:middle_index+1]
    right = data[middle_index+1:right_index+1]
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            data[left_index] = left[i]
            i += 1
        else:
            data[left_index] = right[j]
            j += 1

        left_index += 1

    while i < len(left):
        data[left_index] = left[i]
        i += 1
        left_index += 1

    while j < len(right):
        data[left_index] = right[j]
        j += 1
        left_index += 1
    pass


def merge_sort_algorithm(data: List[int]) -> Tuple[List[int], int]:
    def _merge_sort(left_index: int, right_index: int) -> int:
        if right_index <= left_index:
            return 0

        middle_index = (left_index + right_index) // 2

        statistic = _merge_sort(left_index, middle_index)
        statistic += _merge_sort(middle_index + 1, right_index)

        statistic += data[left_index] + data[middle_index] + data[right_index]
        merge_sorted_subarrays(data, left_index, middle_index, right_index)
        statistic += data[left_index] + data[middle_index] + data[right_index]

        return statistic

    result_statistic = _merge_sort(0, len(data) - 1)

    return data, result_statistic
