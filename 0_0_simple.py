def mean(values):
    """Calculate and return the 
    arithmetic mean of a list
    of numbers."""
    return (sum(values, 0.0) / 
            len(values))

list1 = [5, 10, 30]
list2 = [5, 10, 20, 5, 5]

print mean.__doc__
print mean(list1), mean(list2)
