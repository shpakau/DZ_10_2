# ### ------------------------------------------------------------------------------------
# Задача 2.
# Реализуйте класс Table, который хранит целые числа в двумерной таблице.
# При инициализации Table(rows, cols) экземпляру передаются число строк и столбцов в таблице.
# Строки и столбцы нумеруются с нуля. Ячейки таблицы инициализируются нулями.
# table.get_value(row, col) — прочитать значение из ячейки со строкой row, столбцом col.
# Если ячейка с индексами row и col не лежит внутри таблицы, нужно вернуть None.
# table.set_value(row, col, value) — записать число в ячейку со строкой row, столбцом col.
# Гарантируется, что в тестах будет в запись только в ячейки внутри таблицы.
# table.n_rows() — вернуть число строк в таблице.
# table.n_cols() — вернуть число столбцов в таблице.
# Формат ввода --------
# Каждый тест представляет собой код, в котором будут использоваться ваш класс.
# Файл c решением необязательно называть solution.py, он будет переименован автоматически.
# Тест запускается с вашим классом, а его вывод сравнивается с правильным решением.
print('Задача № 2')


class Table(object):

    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self._table = [[0] * cols for _ in range(rows)]

    def get_value(self, row, col):
        return (self._table[row][col] if 0 <= row < self._rows and 0 <= col < self._cols
                else None)

    def set_value(self, row, col, value):
        self._table[row][col] = value

    def n_rows(self):
        return self._rows

    def n_cols(self):
        return self._cols

    def delete_row(self, row):
        self._table.pop(row)
        self._rows -= 1

    def delete_col(self, col):
        for row in range(self._rows):
            self._table[row].pop(col)
        self._cols -= 1

    def add_row(self, row):
        self._table.insert(row, [0] * self._cols)
        self._rows += 1

    def add_col(self, col):
        for row in range(self._rows):
            self._table[row].insert(col, 0)
        self._cols += 1


def main():
    print('Пример №1')
    tab = Table(3, 5)
    tab.set_value(0, 1, 10)
    tab.set_value(1, 2, 20)
    tab.set_value(2, 3, 30)
    for i in range(tab.n_rows()):
        for j in range(tab.n_cols()):
            print(tab.get_value(i, j), end=' ')
        print()
    print()

    tab.add_row(1)

    for i in range(tab.n_rows()):
        for j in range(tab.n_cols()):
            print(tab.get_value(i, j), end=' ')
        print()
    print()

    print('Пример №2')
    tab = Table(2, 2)

    for i in range(tab.n_rows()):
        for j in range(tab.n_cols()):
            print(tab.get_value(i, j), end=' ')
        print()
    print()

    tab.set_value(0, 0, 10)
    tab.set_value(0, 1, 20)
    tab.set_value(1, 0, 30)
    tab.set_value(1, 1, 40)

    for i in range(tab.n_rows()):
        for j in range(tab.n_cols()):
            print(tab.get_value(i, j), end=' ')
        print()
    print()

    for i in range(-1, tab.n_rows() + 1):
        for j in range(-1, tab.n_cols() + 1):
            print(tab.get_value(i, j), end=' ')
        print()
    print()

    tab.add_row(0)
    tab.add_col(1)

    for i in range(-1, tab.n_rows() + 1):
        for j in range(-1, tab.n_cols() + 1):
            print(tab.get_value(i, j), end=' ')
        print()
    print()

    print('Пример №3')
    tab = Table(1, 1)

    for i in range(tab.n_rows()):
        for j in range(tab.n_cols()):
            print(tab.get_value(i, j), end=' ')
        print()
    print()

    tab.set_value(0, 0, 1000)

    for i in range(tab.n_rows()):
        for j in range(tab.n_cols()):
            print(tab.get_value(i, j), end=' ')
        print()
    print()

    for i in range(-1, tab.n_rows() + 1):
        for j in range(-1, tab.n_cols() + 1):
            print(tab.get_value(i, j), end=' ')
        print()
    print()

    tab.add_row(0)
    tab.add_row(2)
    tab.add_col(0)
    tab.add_col(2)

    tab.set_value(0, 0, 2000)
    tab.set_value(0, 2, 3000)
    tab.set_value(2, 0, 4000)
    tab.set_value(2, 2, 5000)

    for i in range(-1, tab.n_rows() + 1):
        for j in range(-1, tab.n_cols() + 1):
            print(tab.get_value(i, j), end=' ')
        print()
    print()


if __name__ == "__main__":
    main()