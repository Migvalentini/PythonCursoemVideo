#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
#No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente

student_class = list()
student = list()

controller = " "
cont = 0

while controller != "N":
    name = str(input(f"Enter the name of the {cont+1}° student: "))
    grade1 = float(input(f"Enter the 1° grade: "))
    grade2 = float(input(f"Enter the 2° grade: "))
    grade_average = (grade1 + grade2) / 2
    student.append(name)
    student.append(grade1)
    student.append(grade2)
    student.append(grade_average)
    student_class.append(student[:])
    student.clear()
    cont += 1
    controller = " "
    while controller not in "YyNn":
        controller = str(input("Enter if you want continue: ").upper().strip()[0])
        
print("\nNo°:    Name:    Grade Average:")        
for i, s in enumerate(student_class):
    print(f"{i}    {student_class[i][0]}    {student_class[i][3]}")

print("\n")    
while True:
    selected_student = int(input("Enter the student you want see the grades: "))
    if selected_student == 999:
        break
    print(student_class[selected_student][1], student_class[selected_student][2])