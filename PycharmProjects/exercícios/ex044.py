compra = float(input("Valor da compra:"))
print("Formas de pagamento ")
forma = int(input("A vista/Cheque digite 1\nCartão digite 2\nCartão em 2x digite 3\nCartao em 3x ou mais digite 4\nEscolha:"))
if forma == 1:
    valor = compra - (compra * 10 / 100)
    print("a compra vai da {}".format(valor))

elif forma == 2:
    valor = compra - (compra * 5 / 100)
    final = valor / 2
    print("a compra da {} em duas vezes".format(final))

elif forma == 3:
    final = compra // 2
    print("a compra da {}".format(final))

elif forma == 4:
    quantos = int(input("em quantas vezes?"))
    valor = compra + (compra * 20 / 100)
    final = valor // quantos
    print("a compra eu {} em {}x".format(final, quantos))
