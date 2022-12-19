numbers = ("zero","one","two","three","four","five","six","seven","eight","nine","ten")
while True:
    num = int(input("Enter a number: "))
    if num >= 0 and num <= 20:
        break
    
print(numbers[num])