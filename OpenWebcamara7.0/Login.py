import Style
import sys # BIBLIOTECA UTILIZADA PARA IMPORTAR ARGUMENTOS / ADMINISTRAR SISTEMA OPERACIONAL
from pywinauto import Desktop
import time # BIBLIOTECA UTILIZADA PARA TIMERS (FAZER O SCRIPT ESPERAR)
import subprocess 
import os

alterar_cor = Style.alterar_cor
usuario = sys.argv[1] # VARIÁVEL DE LOGIN (USUARIO) QUE VEM DO MAIN.PY
senha = sys.argv[2] # VARIÁVEL DE LOGIN (SENHA) QUE VEM DO MAIN.PY
exe = sys.argv[3] # VARIÁVEL DO CAMINHO DO EXE QUE VEM DO MAIN.PY

print(alterar_cor(f"\nCaminho selecionado: {exe}", "green", "sim"))

if os.path.exists(exe) == True:
    print(alterar_cor(f"\nExecutável encontrado!", "blue", "sim"))
    subprocess.Popen([exe]) # MANDO O SUBPROCESS ABRIR O EXECUTÁVEL
else:
    print(f"\nExecutável não encontrado pelo Pywinauto! (Verifique a formatação utilizada)")
    input("")
    sys.exit()

login = Desktop(backend="win32").window(class_name="TLogin_") # LOCALIZA A JANELA DE LOGIN PELA CLASSE "TLogin_"
controles = login.children() # DEFINO A LISTA DE CONTROLES / BOTOES DA PÁGINA DE LOGIN

botaologin = login.child_window(class_name="TEdit") # LOCALIZA O BOTAO DE LOGIN PELA CLASSE
botaosenha = login.child_window(class_name="TMaskEdit") # LOCALIZA O BOTAO DE SENHA PELA CLASSE

while not login.exists():
    time.sleep(0.1)
login.wait("ready", timeout=12)

botaologin.click_input() # MANDO O PYWINAUTO CLICAR NO BOTAO DE USUARIO
botaologin.set_edit_text("")
botaologin.set_edit_text(usuario)

botaosenha.click_input() # MANDO O PYWINAUTO CLICAR NO BOTAO DE SENHA
botaosenha.set_edit_text(senha)

botaoentrar = login.child_window(title="OK")

while not botaoentrar.exists():
    time.sleep(0.1)
botaoentrar.wait("ready", timeout=3)
time.sleep(1)
botaoentrar.click() # MANDO O PYWINAUTO CLICAR NO BOTAO DE "OK" (PARA REALIZAR O LOGIN)
sys.exit()
