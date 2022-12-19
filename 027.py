nome =  str(input("Digite seu ome Completo: ")).strip()

n = nome.split()

print("O primeiro nome é",n[0])
print("O seu último nome é",n[len(n)-1])