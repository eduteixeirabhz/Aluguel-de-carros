d = int(input("O carro será alugado por quantos dias? "))
km = float(input('Quanto Km percorridos? '))
p = (d * 60) + (km * 0.15)
print("O valor total é de {:.2f} reais".format(p))
