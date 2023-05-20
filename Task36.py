def print_operation_table(operation, num_rows=6, num_columns=6):
    print()
    print("{:^6} |".format(""), end="")
    for col in range(1, num_columns+1):
        print("{:^6}".format(col), end=" |")
    print()

    print("{}-{}{}".format("-" * 7, "-" * 7 * num_columns, "-"))

    # печатаем значения таблицы
    for row in range(1, num_rows+1):
        print("{:^6} |".format(row), end="")
        for col in range(1, num_columns+1):
            value = operation(row, col)
            print("{:^6}".format(value), end=" |")
        print()

def multiply(x, y):
    return x * y

print_operation_table(multiply)

print()