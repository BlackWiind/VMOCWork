"""
 Курсовая работа по дисциплине 'Алгоритмы и вычислительные методы оптимизации'
 Решение задачи линейного программирования симплекс методом
 """

table: list = [
    [6, 2, 3],
    [1, 1, 0],
    [1, -1, 1]
]

x0: list = [0, 0, 6, 1, 1]

z: list = [0, -1, -2]


def check_solution(z: list) -> bool:
    for value in z:
        if value < 0: return False


def find_column(some_array: list) -> int:
    abs_list = [abs(c) for c in some_array]
    return abs_list.index(max(abs_list))


def find_row(table: list, row_index: int) -> int:
    dop_column: list = [row[0] / row[row_index] for row in table if row[row_index] != 0]
    return min(dop_column)


def rectangle_rule(first: float, second: float, third: float, fourth: float) -> float:
    return first - (second * third / fourth)


def main():
    while not check_solution(z):
        pass


if __name__ == '__main__':
    print(find_row(table, 2))
    # main()
