import Config
import Style
import time
import os

CORPADRAO = Config.CORPADRAO
TAMANHOPADRAO = Config.TAMANHOPADRAO
os.system(CORPADRAO)
os.system(TAMANHOPADRAO)
alterar_cor = Style.alterar_cor
loading = Style.loading

bannerp1 = """
====================================================================================
    ___                 __        __   _       ____
   / _ \ _ __   ___ _ _ \ \      / /__| |__  /  ___|___  _ __ _    __ _ _ __ __ _
   | | | | '_ \ / _ \ '_ \ \ /\ / / _ \ '_ \| |   / _` | '_ ` _ \ / _` | '__/ _` |
   | |_| | |_) |  __/ | | \ V  V /  __/ |_) | |__| (_| | | | | | | (_| | | | (_| |
   \___/ | .__/ \___|_| |_|\_/\_/ \___|_.__/ \____\__,_|_| |_| |_|\__,_|_|  \__,_|
         |_|
====================================================================================
⠀                                                                        Versão 6.0⠀                                                       
"""
bannerp2 = """        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣏⡦⠤⣤⠽⠤⡄
    ⡴⠋⠙⢦⠀⠀⠀⠀⠀⣀⡤⠤⠣⢈⠇⠀⠁⣠⡿⡄
    ⠀⠀⣠⠏⠀⠀⡠⠂⠉⠀⠀⠀⠀⠀⢀⡀⠈⠀⠀⠈
    ⡴⠋⠀⠀⠀⡔⠀⠀⠀⠀⠀⡀⠀⡰⣯⡀⠀⠀⠀⠀
    ⡇⠀⠀⠀⢰⠁⠀⠀⠀⠀⠀⡹⠂⢽⠎⠁⠀⠀⠀⠀
    ⢳⠀⠀⠀ ⠃⣴⠀⠀⢀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠙⢦⣤⣤⣬⡷⣣⠌⣁⠐⠋⠂                                                     
"""

for caractere in bannerp1:
    print(caractere, end="", flush=True)
    time.sleep(0.001)

for caractere in bannerp2:
    print(alterar_cor(caractere, "green", "sim"), end="", flush=True)
    time.sleep(0.001)

loading(alterar_cor(' '*80, "white", "nao"))
