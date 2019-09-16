prompt = "Insert number 1: "
number1= input(prompt)
number1= int(number1)
prompt= "Insert number 2: "
number2= input(prompt)
number2= int(number2)

operator= input("Insert operation: ")
result= eval(f'{number1}{operator}{number2}')

print(f' The result is = {result}')