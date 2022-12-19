#Aprimore o desafio anterior, mostrando no final: 
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

array = [[0,0,0],[0,0,0],[0,0,0]]
sum_even = sum_column_3 = biggest_line_2 = 0

for line in range(0, 3):
    for column in range(0, 3):
        array[line][column] = int(input(f"Enter a number [{line}x{column}]: "))
        if array[line][column] % 2 == 0:
            sum_even += array[line][column]
        if column == 2:
            sum_column_3 += array[line][column]
        if line == 1 and array[line][column] > biggest_line_2:
            biggest_line_2 = array[line][column]

for line in range(0, 3):
    for column in range(0, 3):
        print(array[line][column], end = " ")
    print()

print(f"The sum of even numbers is {sum_even}")
print(f"The sum of the values in the third column is {sum_column_3}")
print(f"The biggest value of second line is {biggest_line_2}")