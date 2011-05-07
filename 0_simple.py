def mean(values):
    """Calculate and return the arithmetic mean of a list of numbers."""
    return sum(values, 0.0) / len(values)

list1 = [5, 10, 30]
list2 = [x*x for x in range(3)]

print mean.__doc__
print list1, "mean:", mean(list1)
print list2, "mean:", mean(list2)
