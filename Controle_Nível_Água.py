Nivel_Agua = int(input("Digite o nível da água: "))

from colorama import Fore, Style

if Nivel_Agua < 20:
    print(Fore.RED + "Muito baixo")

elif Nivel_Agua >= 21 and Nivel_Agua <= 40:
    print(Fore.YELLOW + "Baixo")


elif Nivel_Agua >= 41 and Nivel_Agua <= 60:
    print(Fore.GREEN + "Médio")

elif Nivel_Agua >= 61 and Nivel_Agua <= 80:
    print(Fore.CYAN + "Alto")

else:
    print(Fore.BLUE + "Muito alto")












