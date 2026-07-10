from colorama import init, Fore
import itertools
import time
import sys

def alterar_cor(texto, cor, claro):
    if texto: 
        match claro.strip().lower():
            case "sim":
                nomecor = f"LIGHT{cor.upper()}_EX"
                coloracao = getattr(Fore, nomecor)
            case "nao":
                nomecor = f"{cor.upper()}"
                coloracao = getattr(Fore, nomecor)
        resultado = (coloracao + f'{texto}')
        return resultado
    else: print('Você chamou a função "alterar_cor" sem usar texto!')


def loading(texto="Carregando", duracao=1.5):
    inicio = time.time()
    for simbolo in itertools.cycle("⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"):
        if time.time() - inicio >= duracao:
            break
        sys.stdout.write(alterar_cor(f"\r{texto} {simbolo}","white", "sim"))
        sys.stdout.flush()
        time.sleep(0.1)
    
    texto = (f"\r{texto} ✔")
    print(alterar_cor(texto, "green", "sim"))