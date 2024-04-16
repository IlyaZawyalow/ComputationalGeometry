import math
import numpy as np


def find_extreme_points(array_points, vectors):
    def compare_points(min_point, point):
        return math.atan2(min_point[1] - point[1], min_point[0] - point[0])

    min_point = min(array_points, key=lambda point: (point[1], point[0]))
    sorted_points = sorted(array_points, key=lambda point: compare_points(min_point, point), reverse=True)

    extreme_points_list = []

    for vector in vectors:

        left_border = 0
        right_border = len(sorted_points) - 1

        while left_border <= right_border:
            avg = (left_border + right_border) // 2
            dot_product = np.dot(vector, sorted_points[(avg + 1) % len(sorted_points)] - sorted_points[avg])

            if dot_product < 0:
                right_border = avg - 1
            else:
                left_border = avg + 1

        extreme_point = sorted_points[(right_border + 1) % len(sorted_points)]
        extreme_points_list.append(list(extreme_point))
    return extreme_points_list


def main():
    with open(f'data.txt', 'r') as file:
        array_points = eval(file.readline())
        vectors = eval(file.readline())
    array_points = np.array(array_points)
    vectors = np.array(vectors)

    with open(f'result.txt', 'w') as file:
        file.write(str(find_extreme_points(array_points, vectors)))


if __name__ == '__main__':
    main()
