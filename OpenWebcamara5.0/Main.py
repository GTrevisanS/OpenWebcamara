from pathlib import Path
import Config
import subprocess
import sys
import os
import time

MINHAPASTA = Config.MINHAPASTA
PASTACLIENTE = Config.PASTACLIENTE
CONFIG_INI = Path(MINHAPASTA) / "configuracao.ini"
ENDERECO_INI = Path(MINHAPASTA) / "endereco_ip_servidor.ini"
LOGIN_SCRIPT = Config.LOGIN_SCRIPT
BANNER_SCRIPT = Config.BANNER_SCRIPT
USUARIOWEBCAM = Config.USUARIOWEBCAM
SENHAWEBCAM = Config.SENHAWEBCAM
IP = Config.IP
DB = Config.DB
DBF = Config.DBF
PORTA = Config.PORTA

def cls():
    os.system("cls")
def pause():
    input("\nPressione ENTER para continuar...")
def ver_conexao_atual():
    with open(CONFIG_INI, encoding="cp1252") as arquivo:
        linhas = arquivo.read().splitlines()

    return linhas[0], linhas[1], linhas[2], linhas[3]
def alterar_ini(caminho, ip, db, dbf, porta):
    with open(caminho, encoding="cp1252") as arquivo:
        linhas = arquivo.readlines()
    linhas[0] = ip + "\n"
    linhas[1] = db + "\n"
    linhas[2] = dbf + "\n"
    linhas[3] = porta + "\n"
    with open(caminho, "w", encoding="cp1252") as arquivo:
        arquivo.writelines(linhas)
def alterar_conexao(ip, db, dbf, porta):
    alterar_ini(CONFIG_INI, ip, db, dbf, porta)
    alterar_ini(ENDERECO_INI, ip, db, dbf, porta)
    print("\n ----- Arquivos atualizados com sucesso -----\n")
def abrir_login(exe):
    subprocess.run(
        [
            "python",
            LOGIN_SCRIPT,
            USUARIOWEBCAM,
            SENHAWEBCAM,
            str(exe)
        ])
def listar_executaveis_para_print(pasta):
    executaveis = sorted(
        Path(pasta).glob("WebCamara*.exe"),
        key=lambda arquivo: arquivo.stat().st_mtime,
        reverse=True
    )
    lista_exe = [arquivo.name for arquivo in executaveis]
    versoes = []
    for item in lista_exe:
        item = str(item).lower().replace('webcamara','').replace('.exe','').strip()
        versoes.append(item)
    return versoes

def listar_executaveis(pasta):
    executaveis = sorted(
        Path(pasta).glob("WebCamara*.exe"),
        key=lambda arquivo: arquivo.stat().st_mtime,
        reverse=True
    )
    return executaveis
def procurar_ultimo_exe(pasta):
    lista = listar_executaveis(pasta)
    if not lista:
        print("\nNenhum executável encontrado.")
    return lista[0]
def procurar_exe_manual(pasta):

    versao = input("Versão: ").strip()
    numero = input("Executável: ").strip()

    candidato = Path(pasta) / f"WebCamara {versao}({numero}).exe"

    if candidato.exists():

        return candidato

    candidato = Path(pasta) / f"WebCamara {versao} ({numero}).exe"

    if candidato.exists():

        return candidato

    candidato = Path(pasta) / f"WebCamara {versao}.exe"

    if candidato.exists():

        return candidato

    print("\nExecutável não encontrado.\n") # No caso de não encontrar NENHUM EXE parecido
    return None
def mostrar_exes():
    cls()
    print("=" * 70)
    print()
    print("1 - Minha Pasta")
    print("2 - Pasta Cliente")
    print("3 - Pasta Personalizada")
    print()
    print("=" * 70)
    escolha = input("> ")

    if escolha == "1":

        pasta = MINHAPASTA

    elif escolha == "2":

        pasta = PASTACLIENTE

    elif escolha == "3":

        pasta = input("Informe a pasta: ")

    else:

        return
    cls()

    print()
    for exe in listar_executaveis(pasta):
        print(exe.name)
    print()
    pause()
def mostrar_conexao(PASTA, OIP, ODB, ODBF, APORTA):
    os.system("color 06")
    cls()
    print("====================================================================================")
    print()
    print("                Conexão atual no arquivo Config.ini                                 ")
    print()
    print("                IP      :", [OIP])
    print("                Banco   :", [ODB])
    print("                Banco 2 :", [ODBF])
    print("                Porta   :", [APORTA])
    print()
    print(f"               Pasta utilizada: {PASTA}")
    print()
    print("====================================================================================")
    print()
    pausar()

def painel():
    os.system("color 0B")
    os.system("mode con: cols=87 lines=20")
    MINHAPASTA = Config.MINHAPASTA
    PASTACLIENTE = Config.PASTACLIENTE
    CONFIG_INI = Path(MINHAPASTA) / "configuracao.ini"
    ENDERECO_INI = Path(MINHAPASTA) / "endereco_ip_servidor.ini"
    LOGIN_SCRIPT = Config.LOGIN_SCRIPT
    BANNER_SCRIPT = Config.BANNER_SCRIPT
    USUARIOWEBCAM = Config.USUARIOWEBCAM
    SENHAWEBCAM = Config.SENHAWEBCAM
    IP = Config.IP
    DB = Config.DB
    DBF = Config.DBF
    PORTA = Config.PORTA
    cls()
    print()
    print("====================================================================================")
    print()
    print('           DEFINA QUE TIPO DE ACÃO VOCE DESEJA REALIZAR PELO PAINEL:                ')
    print()
    print('           WebCamara Homologacão              DIGITE...        [1]                  ')        
    print('           Conexão rápida (apenas abrir)      DIGITE...        [2]                  ')
    print('           Conexão Personalizada              DIGITE...        [3]                  ')
    print('           WebCamara Cliente                 DIGITE...        [4]                  ') 
    print('           Verificar Conexão atual            DIGITE...        [0]                  ') 
    print()
    # print('      Rodar WebUpload                    DIGITE...        [W]     ') 
    print('           Listar todos os EXE´s              DIGITE...        [E]                  ') 
    print()
    print("====================================================================================")


    RESPOSTA = input("\n> ")
    RESPOSTA = str(RESPOSTA).lower().strip()

    match RESPOSTA:
        case "1":
            alterar_conexao(IP,DB,DBF,PORTA)
            print("Abrindo Versão mais recente do Homologação...")
            EXE = (procurar_ultimo_exe(MINHAPASTA))
            subprocess.Popen([
                "python",
                "Login.py",
                USUARIOWEBCAM,
                SENHAWEBCAM,
                str(EXE)])
            sys.exit()
        case "2":
            while True:
                PERGUNTA = input("\nDeseja escolher o executável? [S/N]: ").strip().lower()
                match PERGUNTA:
                    case "s":
                        EXE = procurar_exe_manual(MINHAPASTA)
                        subprocess.Popen([
                            "python",
                            "Login.py",
                            USUARIOWEBCAM,
                            SENHAWEBCAM,
                            str(EXE)
                        ])
                        sys.exit()
                    case "n":
                        EXE = procurar_ultimo_exe(MINHAPASTA)
                        subprocess.Popen([
                            "python",
                            "Login.py",
                            USUARIOWEBCAM,
                            SENHAWEBCAM,
                            str(EXE)
                        ])
                        sys.exit()
                    case _:
                        print("\nOpção inválida. Digite apenas S ou N.")
        case "3":
            IP = input("\nIP: ").replace(" ","")
            PORTA = input("Porta: ").replace(" ","")
            print()
            DB = input("Nome do Banco de registros: ").replace(" ","").lower()
            DBF = input("Nome do Banco de arquivos: ").replace(" ","").lower()
            if IP == "" or PORTA == "" or DB == "" or DBF == "":
                print("\n----- OPS, ALGUM CAMPO FICOU VAZIO, TENTE NOVAMENTE! -----\n")
                pause()
                painel()
            alterar_conexao(IP,DB,DBF,PORTA)
            EXE = procurar_exe_manual(MINHAPASTA)
            subprocess.Popen([
                "python",
                "Login.py",
                USUARIOWEBCAM,
                SENHAWEBCAM,
                str(EXE)])
            painel()
            sys.exit()
        case "4":
            EXE = procurar_ultimo_exe(PASTACLIENTE)
            subprocess.Popen([
                "python",
                "Login.py",
                USUARIOWEBCAM,
                SENHAWEBCAM,
                str(EXE)])
            sys.exit()
        case "0":
            ip, db, dbf, porta = ver_conexao_atual()
            cls()
            print()
            print("====================================================================================")
            print()
            print('            CONEXÃO ATUAL DA SUA PASTA ABAIXO')
            print()
            print(f"            IP:         {ip}")
            print(f"            DB1:        {db}")
            print(f"            DB2:        {dbf}")
            print(f"            PORTA:      {porta}")
            print()
            print(f'            Dados sendo coletados de:   "{MINHAPASTA}"')
            print()
            print("====================================================================================")
            print()
            pause()
            painel() 
        case "e":
            while True:
                cls()
                print()
                print("====================================================================================")
                print()
                print("                  [Defina a pasta em que deseja listar os EXE abaixo]")
                print()
                print("                  Minha Pasta                         DIGITE...    [1]")
                print("                  Pasta Cliente                       DIGITE...    [2]")
                print("                  Pasta Personalizada                 DIGITE...    [3]")
                print()
                print("                  Busca filtrada na minha pasta       DIGITE...    [B]")
                print()
                print("====================================================================================")
                QUAL = input("\n> ")
                QUAL = str(QUAL).lower().strip()
                CONTADOR = 8
                match QUAL:
                    case "1":
                        lista = listar_executaveis_para_print(MINHAPASTA)
                        for i in lista:
                            CONTADOR+=1
                        os.system(f"mode con: cols=87 lines={CONTADOR}")
                        break
                    case "2":
                        lista = listar_executaveis_para_print(PASTACLIENTE)
                        for i in lista:
                            CONTADOR+=1
                        os.system(f"mode con: cols=87 lines={CONTADOR}")
                        break
                    case "3":
                        SELECIONADA = input("\nDigite o caminho da pasta que deseja listar: ")
                        lista = listar_executaveis_para_print(SELECIONADA)
                        for i in lista:
                            CONTADOR+=1
                        os.system(f"mode con: cols=87 lines={CONTADOR}")
                        break
                    case "b":
                        SELECIONADA = input("\nDigite o caminho da pasta que deseja listar: ")
                        lista = listar_executaveis_para_print(SELECIONADA)
                        for i in lista:
                            CONTADOR+=1
                        os.system(f"mode con: cols=87 lines={CONTADOR}")
                        break
                    case _:
                        pass
            print()
            print('='*30,f"{CONTADOR-8} VERSÕES DISPONÍVEIS",'='*30)
            print()
            for versao in lista:
                print(">",versao)
            print()
            print('='*87)
            input()
            painel()    
        case _:
            painel() 

painel()