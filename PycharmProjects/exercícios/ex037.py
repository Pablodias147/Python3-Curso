num = int(input('Digite o número que deseja converter: '))
opção = int(input('Escolha qual a base de conversão você quer usar, 1 para binário, 2 para octal e 3 para hexadecimal: '))
if opção== 1:
    print("{} convertido para binario é igual {}".format(num, bin(opção)[2:]))
elif opção == 2:
    print("{} convertido para octal é {}".format(num, oct(opção)[2:]))
elif opção == 3:
    print("{} convertido para hexadecimal é {}".format(num, hex(opção)[2:]))
else: print("Opção invalida, Tente novamente")
