import sys # BIBLIOTECA UTILIZADA PARA IMPORTAR ARGUMENTOS / ADMINISTRAR SISTEMA OPERACIONAL
from pywinauto import Desktop
import time # BIBLIOTECA UTILIZADA PARA TIMERS (FAZER O SCRIPT ESPERAR)
import subprocess 

usuario = sys.argv[1] # VARIÁVEL DE LOGIN (USUARIO) QUE VEM DO .BAT
senha = sys.argv[2] # VARIÁVEL DE LOGIN (SENHA) QUE VEM DO .BAT
exe = sys.argv[3] # VARIÁVEL DO CAMINHO DO EXE QUE VEM DO .BAT

subprocess.Popen(exe) # MANDO O SUBPROCESS ABRIR O EXECUTÁVEL

login = Desktop(backend="win32").window(class_name="TLogin_") # LOCALIZA A JANELA DE LOGIN PELA CLASSE "TLogin_"
controles = login.children() # DEFINO A LISTA DE CONTROLES / BOTOES DA PÁGINA DE LOGIN

botaologin = login.child_window(class_name="TEdit") # LOCALIZA O BOTAO DE LOGIN PELA CLASSE
botaosenha = login.child_window(class_name="TMaskEdit") # LOCALIZA O BOTAO DE SENHA PELA CLASSE

time.sleep(2.5)  

botaologin.click_input() # MANDO O PYWINAUTO CLICAR NO BOTAO DE USUARIO
botaologin.set_edit_text("") # LIMPO O QUE ESTA ESCRITO
botaologin.type_keys(usuario, with_spaces=True) # DIGITO O USUARIO IMPORTADO DO .BAT

botaosenha.click_input() # MANDO O PYWINAUTO CLICAR NO BOTAO DE SENHA
botaosenha.type_keys(senha, with_spaces=True) # DIGITO A SENHA IMPORTADA DO .BAT

login.child_window(title="OK").click_input() # MANDO O PYWINAUTO CLICAR NO BOTAO DE "OK" (PARA REALIZAR O LOGIN)

sys.exit()