temp = float(input("Informe a temperatura: "))

option = int(input("Deseja converter para Celsius ou Fahrenheit? [1 | 2]: "))

if option == 1:
    temp = (temp - 32) * 5 / 9
    print(f"Temperatura em Celsius: {temp}°")
elif option == 2: 
    temp = round((temp * 1.8) + 32, 1)
    print(f"Temperatura em Fahrenheit: {temp}°")
else:
    print("Opção inválida")