valor_compra = float(input("Informe o valor da compra: R$ "))

if valor_compra > 250:
    valor_desconto = valor_compra * 0.16
    valor1 = valor_compra - valor_desconto
    print(f"O seu valor depois do desconto de 16% ficou em: R$ {valor1}")
    print(f"Seu desconto foi de: R$ {valor_desconto: .2f}")
else:
    print(f"O seu valor ficou em: R$ {valor_compra}")