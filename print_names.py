import sys

# Проверяем, передан ли аргумент
if len(sys.argv) > 1:
    name = sys.argv[1]
    print(f"Hello, {name}!")
else:
    print("No name provided!")
