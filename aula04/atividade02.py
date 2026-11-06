vendas = float(input("Informe o valor total de vendas: R$ "))
salario = float(input("Informe seu salário: R$ "))

if vendas >= 1000:
    salario1 = salario + 150
    print(f"O seu bônus foi de R$ 150.00 e o seu salário ficou em: R$ {salario1}")

elif vendas >= 500:
    salario2 = salario + 75
    print(f"O seu bônus foi de R$ 75.00 e o seu salário ficou em: R$ {salario2}")

else:
    print(f"Você não obteve bônus e o seu salário ficou em: R$ {salario}")