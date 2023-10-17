import sys

names = sys.argv
names.pop(0)

for index, item in enumerate(names, start=1):
    string_to_print = f"{index}. {item}"
    print(string_to_print)
    