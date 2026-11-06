ano_nascimento = int(input("Informe o ano de nascimento: "))

idade = 2026 - ano_nascimento

if idade >= 18:
    print("Você é maior.")
else:
    print("Você é menor.")