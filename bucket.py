from typing import List


def bucket_sort(patterns: List[str], prefix_length: int) -> List[None]:
    buckets = {}

    for i, pattern in enumerate(patterns):
        prefix = pattern[:prefix_length]
        if prefix not in buckets:
            buckets[prefix] = []
        buckets[prefix].append((i, pattern))

    for bucket in buckets.values():
        bucket.sort(key=lambda x: x[1])

    positions = [None] * len(patterns)
    global_position = 0

    for bucket in sorted(buckets.keys()):
        local_position = 0
        for original_index, pattern in buckets[bucket]:
            positions[original_index] = (global_position, local_position)
            global_position += 1
            local_position += 1

    return positions
