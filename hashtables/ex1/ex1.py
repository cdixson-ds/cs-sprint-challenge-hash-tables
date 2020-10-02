
weights = [ 4, 6, 10, 15, 16 ]
length = 5
limit = 21



def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    cache = {}
    if len(weights) <= 1:
        return None

    for index in range(length):
        value = weights[index]

        #returns value and index if in the cache
        if value in cache:
            cache_index = cache[value]
            return(index, cache_index)

        diff = limit - weights[index]
        cache[diff] = index

    return None


print(get_indices_of_item_weights(weights, length, limit))
 

        







    