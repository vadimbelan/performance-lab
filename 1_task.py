import sys


def find_path(n, m):
    visited = set()
    path = []
    current_index = 0

    while current_index not in visited:
        visited.add(current_index)
        path.append(str(current_index + 1))
        current_index = (current_index + m - 1) % n

    return ''.join(path)


def main():
    if len(sys.argv) != 5:
        print("python3 1_task.py <n1> <m1> <n2> <m2>")
        sys.exit(1)

    try:
        n1 = int(sys.argv[1])
        m1 = int(sys.argv[2])
        n2 = int(sys.argv[3])
        m2 = int(sys.argv[4])
    except ValueError:
        raise ValueError("Все аргументы должны быть целыми числами")

    if n1 <= 0 or m1 <= 0 or n2 <= 0 or m2 <= 0:
        print("Все числа должны быть больше 0")
        sys.exit(1)

    path1 = find_path(n1, m1)
    path2 = find_path(n2, m2)
    print(path1 + path2)


if __name__ == "__main__":
    main()
