"""
In this module I'm Trying to make a cartesian product of a argument that has been passed to the method.
For Example:
>>> cartesian_product([0, 1], repeat=2)
>>> # should give us something like:
>>> [(0, 0), (0, 1), (1, 0), (1, 1)]

Note: remmember that this function is a generator function and yield data. So use it carefully.
"""
def cartesian_product(*args, repeat=1):
    stations = [tuple(i) for i in args] * repeat
    result = [[]]
    for station in stations:
        result = [x+[y] for x in result for y in station]
    for station in result:
        yield tuple(station)