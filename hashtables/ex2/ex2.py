#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    cache = {}
    route = [None] * length
    
    #store tickets in cache
    for t in tickets:
        cache[t.source] = t.destination

    #source of none for first ticket
    ticket1 = cache["NONE"]

    #loop over to add flights
    for flight in range(length):
        route[flight] = ticket1
        ticket1 = cache[ticket1]

    return route
