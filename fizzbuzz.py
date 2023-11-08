import sys

numbers = sys.argv
numbers.pop(0)

for item in numbers:
    item = int(item)
    if item % 3 == 0 and item % 5 == 0:
        print('fizzbuzz')
    elif item % 3 == 0:
        print('fizz')
    elif item % 5 == 0 :
        print('buzz')
    else:
        print(item)