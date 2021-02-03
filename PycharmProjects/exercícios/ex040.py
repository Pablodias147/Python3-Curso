nota1 = float(input("Diga a sua primeira nota:"))
nota2 = float(input("Diga a sua segunda nota:"))
media = (nota1 + nota2) / 2
if media < 5.0:
    print("Voce foi reprovado")
elif media > 7.0:
    print("voce foi aprovado")
elif media >= 5.0 or 6.9:
    print("voce esta em recuperação")

