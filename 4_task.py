import sys


def find_min_moves(nums, max_moves=20):
    if not nums:
        raise ValueError("Массив пуст")

    nums_sorted = sorted(nums)
    median = nums_sorted[len(nums_sorted) // 2]
    moves = sum(abs(num - median) for num in nums)

    # Разбил длинную строку на две части (E501 line too long).
    msg = (
        f"{max_moves} ходов недостаточно для приведения "
        "всех элементов массива к одному числу"
    )
    return moves if moves <= max_moves else msg


def read_numbers(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return [int(line.strip()) for line in file if line.strip()]
    except OSError:
        raise OSError("Файл не найден")
    except ValueError:
        raise ValueError("Файл должен содержать целые числа")


def main():
    if len(sys.argv) != 2:
        # /Users/vadimbelan/Developer/Белан-Вадим-test-tasks/txts/4_test_nums.txt
        print("python3 4_task.py <nums.txt>")
        sys.exit(1)

    try:
        numbers = read_numbers(sys.argv[1])
        result = find_min_moves(numbers)
        print(result)
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
