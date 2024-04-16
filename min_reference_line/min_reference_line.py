import math
from fractions import Fraction

def vector_product(point1, point2, point3):
    A = [point2[0] - point1[0], point2[1] - point1[1]]
    B = [point3[0] - point1[0], point3[1] - point1[1]]
    val = A[0] * B[1] - A[1] * B[0]
    return val

def distance(point1, point2):
    x = point1[0] - point2[0]
    y = point1[1] - point2[1]
    return x**2 + y**2

def compare_points(min_point, point):
    return math.atan2(point[1]-min_point[1], point[0]-min_point[0])

def get_convex_hull(array_points):
    min_point = min(array_points, key=lambda point: (point[1], point[0]))
    array_points.remove(min_point)
    sorted_points = sorted(array_points, key=lambda point: (compare_points(min_point, point), distance(min_point, point)))
    stack = [min_point, sorted_points[0]]
    for i in range(1,len(sorted_points)):
        while len(stack) > 1 and vector_product(stack[-2], stack[-1], sorted_points[i]) <= 0:
            stack.pop()
        stack.append(sorted_points[i])
    array_points.append(min_point)
    return stack

def get_min_reference_line(array_points, convex_hull):
    n = len(array_points)
    mean_x = Fraction(sum(point[0] for point in array_points), n)
    mean_y = Fraction(sum(point[1] for point in array_points), n)
    min_reference_line = {'min_distance': float('inf'), 'line': None}
    for i in range(len(convex_hull)):
        line = [convex_hull[i], convex_hull[(i+1)%len(convex_hull)]]
        product = vector_product(line[0], line[1], [mean_x, mean_y])
        length = distance(line[0], line[1])
        min_distance = Fraction(product**2, length)
        if min_distance < min_reference_line['min_distance']:
            min_reference_line['min_distance'] = min_distance
            min_reference_line['line'] = line
    return min_reference_line

def main():
    with open(f'data.txt', 'r') as file:
        array_points = eval(file.readline())
    convex_hull = get_convex_hull(array_points)
    min_reference_line = get_min_reference_line(array_points, convex_hull)
    print(min_reference_line)
    with open(f'result.txt', 'w') as file:
        file.write(str(min_reference_line['line']))

if __name__ == '__main__':
    main()