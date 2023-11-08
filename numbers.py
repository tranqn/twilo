import sys

first_number = int(sys.argv[1])
seconde_number = int(sys.argv[2])

result_sum = first_number + seconde_number
result_difference = first_number - seconde_number
result_product = first_number * seconde_number
result_quotient = first_number / seconde_number


print(f"{first_number} + {seconde_number} = {result_sum}")
print(f"{first_number} - {seconde_number} = {result_difference}")
print(f"{first_number} * {seconde_number} = {result_product}")
print(f"{first_number} / {seconde_number} = {result_quotient}")

