def max_repeated_chars(line):
    return max(line.count(char) for char in set(line))

def find_line_with_most_repeats(lines):
    max_line = max(lines, key=max_repeated_chars)
    print(f"Рядок з найбільшою кількістю однакових символів: {max_line}")

N = int(input("Введіть кількість рядків: "))
lines = [input(f"Введіть рядок {i+1}: ") for i in range(N)]
find_line_with_most_repeats(lines)
