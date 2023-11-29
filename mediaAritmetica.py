from os import system, name
system('cls') if(name == 'nt') else system('clear')
print("Média Aritmética")
n1 = float(input("Informe a 1ª nota: "))
n2 = float(input("Informe a 2ª nota: "))
n3 = float(input("Informe a 3ª nota: "))
n4 = float(input("Informe a 4ª nota: "))
media=(n1+n2+n3+n4)/4
print(f"A média de:{n1} | {n2} | {n3} | {n4}:{media:.2f}")

