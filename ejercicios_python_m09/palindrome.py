
texto = input("Ingrese una palabra: ")
reverse = texto[::-1]


if texto == reverse:
    print("La palabra ingresada si es palindromo")
else:
    print("La palabra ingresada no es palindromo")


