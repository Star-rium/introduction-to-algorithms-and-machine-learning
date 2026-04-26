# super naive and unoptimized solution for cartesian product
ranges = [
    ['a'],
    [1, 2, 3],
    ['Y', 'Z']
]

points = [
    []
]

for arr in ranges:
    new_points = [] # new list to overwrite points for each iteration
    for x in points:
        for y in arr:
            new_points.append(x + [y]) # add new elements to the values in points
    points = new_points # overwrite previous result list

print(points)

# For further optimization (big ranges and stuffs), just use itertools.product as it uses almost zero extra memory.


    