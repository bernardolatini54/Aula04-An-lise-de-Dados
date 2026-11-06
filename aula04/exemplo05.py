compra = float(input("Valor da compra: R$ "))
cliente_frequente = input("Programa de fidelidade? [S/N]: ").lower()[0]
print(cliente_frequente)

if compra > 100 or cliente_frequente == "s":
    print("Recebe brinde!")

else:
    print("Sem brinde.")