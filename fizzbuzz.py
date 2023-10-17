import sys

numbers = sys.argv
numbers.pop(0)

for item in numbers:
    if item % 3 == 0:
        print('fizz')
    if item % 5 == 0 :
        print('buzz')
    if item % 3 == 0 and item % 5 == 0:
        print('fizzbuzz')
    else:
        print(item)