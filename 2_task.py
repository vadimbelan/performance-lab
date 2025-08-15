import sys

MIN_VALUE = 1e-38  # 0.00000000000000000000000000000000000001
MAX_VALUE = 1e38  # 100000000000000000000000000000000000000
MAX_POINTS = 100
EPSILON = 1e-7


def is_valid_coordinate(value):
    return value == 0 or MIN_VALUE <= abs(value) <= MAX_VALUE


def validate_ellipse_params(center, radius):
    if len(center) != 2:
        raise ValueError("В первой строке должно быть две координаты")
    if not all(is_valid_coordinate(c) for c in center):
        raise ValueError("Центр должен быть в диапазоне от 1e-38 до 1e38")

    if len(radius) != 2:
        raise ValueError("Во второй строке должно быть две координаты")
    if radius[0] <= 0 or radius[1] <= 0:
        raise ValueError("Радиусы должны быть больше 0")
    if not all(MIN_VALUE <= r <= MAX_VALUE for r in radius):
        raise ValueError("Радиус должен быть в диапазоне от 1e-38 до 1e38")


def read_ellipse_params(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        if len(lines) < 2:
            raise ValueError("<ellipse.txt> должен содержать две строки")

        center = list(map(float, lines[0].split()))
        radius = list(map(float, lines[1].split()))

        validate_ellipse_params(center, radius)

        return center, radius


def validate_points(points):
    if len(points) < 1 or len(points) > MAX_POINTS:
        raise ValueError(f"Количество точек должно быть от 1 до {MAX_POINTS}")
    for point in points:
        if len(point) != 2 or not all(is_valid_coordinate(c) for c in point):
            raise ValueError("Точки должны быть в диапазоне от 1e-38 до 1e38")


def read_points(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        points = [
            list(map(float, line.split()[:2]))
            for line in file
            if len(line.split()) >= 2
        ]
        validate_points(points)
        return points


def find_point_position(center, radius, point):
    h, k = center
    a, b = radius
    x, y = point

    dx = (x - h) / a
    dy = (y - k) / b

    value = dx**2 + dy**2

    if abs(value - 1) <= EPSILON:
        return 0  # Точка лежит на эллипсе.
    elif value < 1:
        return 1  # Точка внутри.
    else:
        return 2  # Точка снаружи.


def main():
    if len(sys.argv) != 3:
        # /Users/vadimbelan/Developer/Белан-Вадим-test-tasks/txts/2_test_ellipse.txt
        # /Users/vadimbelan/Developer/Белан-Вадим-test-tasks/txts/2_test_points.txt
        print("python3 2_task.py <ellipse.txt> <points.txt>")
        sys.exit(1)

    ellipse_file = sys.argv[1]
    points_file = sys.argv[2]

    try:
        center, radius = read_ellipse_params(ellipse_file)
        points = read_points(points_file)

        results = [
            find_point_position(center, radius, point)
            for point in points
        ]
        print("\n".join(map(str, results)))
    except (OSError, ValueError) as e:
        print(f"Ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
