
test = [
    [1, 2, 3, 4, 5],
    [12, 7, 2, 9, 1],
    [99, 2, 7, 1,]
]

def intersection(arrays):
    """
    And we need to compute the _intersection_, that is, numbers that exist
    in all lists.
    """
    cache = {}
    result = []

    count = 1

    for arr in arrays:
        for i in arr:
            if i not in cache:
                cache[i] = count
            else:
                cache[i] += 1

    for j in cache:
        if cache[j] == len(arrays):
            result.append(j)

    return result

#print(intersection(test))


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
