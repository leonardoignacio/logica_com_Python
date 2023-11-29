from os import system, name
system('cls') if(name == 'nt') else system('clear')
multa = 0
diferenca = 0
taxa = 4
limite = 50
print("Cálculo p/ Pescaria")
kg = float(input("Informe quantos Kgs de peixe: "))
if (kg > limite):
    diferenca = kg - limite
    multa = diferenca * taxa
print(f'Cálculo p/ Pescaria')
print(f'A quantidade pescada foi: {kg:.2f}kg')
print(f'A diferença entre o limite é: {diferenca:.2f}')
print(f'O valor de multa é:R${multa:.2f}')


        