num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if num1 == num2 :
    print("Los números son iguales.")
elif num1 < num2 :
    print("El número " + str(num1) + " es menor.")
elif num2 < num1 :
    print("El número " + str(num2) + " es menor.")
else :
    print("...")
