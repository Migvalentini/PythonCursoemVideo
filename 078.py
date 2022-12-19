#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e 
#as suas respectivas posições na lista. 

list = []

for pos in range(5):
    number = float(input("Enter a number: "))
    list.append(number)
    if pos == 0:
        biggest = smallest = list[pos]
    if list[pos] > biggest:
        biggest = list[pos]
    else:
        if list[pos] < smallest:
            smallest = list[pos]
            
print("The positions of the biggest number is: ")
for i, v in enumerate(list):
    if v == biggest:
        print(f"{i}...", end = '')
    
print(f"\nThe biggest number is: {biggest}")
print(f"The smallest number is: {smallest}")