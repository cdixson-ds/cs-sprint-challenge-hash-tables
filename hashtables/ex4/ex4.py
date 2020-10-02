def has_negatives(a):
    """
    For an input list of integers, we wish to know which positive numbers
    have corresponding negative numbers in the list.
    """
   
    cache = {}
    result = []

    count = 1

    #pos greater than zero, add to cache
    for number in a:
        if number > 0:
            if number not in cache:
                cache[number] = count
    
    #neg less than, take absolute value and append to results
    for number in a:
        if number < 0:
            number = abs(number)
            if number in cache:
                result.append(number)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
