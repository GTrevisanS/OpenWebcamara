import Config # Meu python que configura os caminhos e variáveis padrão
import Style
import time
import sys
import os
from pathlib import Path
import subprocess

BASE_DIR = Path(__file__).resolve().parent
LAST_ACCESS = BASE_DIR / "last_acess.txt"
MINHAPASTA = Config.MINHAPASTA
PASTACLIENTE = Config.PASTACLIENTE
CONFIG_INI = Path(MINHAPASTA) / "configuracao.ini"
ENDERECO_INI = Path(MINHAPASTA) / "endereco_ip_servidor.ini"
USUARIOWEBCAM = Config.USUARIOWEBCAM
SENHAWEBCAM = Config.SENHAWEBCAM
IP = Config.IP
DB = Config.DB
DBF = Config.DBF
PORTA = Config.PORTA
alterar_cor = Style.alterar_cor
loading = Style.loading


def cls():
    os.system("cls")

def pause():
    input("\nPressione ENTER para continuar...")


def somente_abrir_exe(EXE):
    os.system(f'start "" {EXE}')


def abrir_login(exe):
    os.system(f'python Login.py "{USUARIOWEBCAM}" "{SENHAWEBCAM}" "{exe}"')


def ver_conexao_atual(arquivo, linhas):
    if linhas == 4:
        with open(arquivo, encoding="cp1252") as arquivo:
            linhas = arquivo.read().splitlines()
        return linhas[0], linhas[1], linhas[2], linhas[3]
    elif linhas == 1:
        with open(arquivo, encoding="cp1252") as arquivo:
            linhas = arquivo.read().splitlines()
        return linhas[0]
    else:
        print("\nVoce esqueceu de definir as linhas!")
        pause()


def alterar_arq(caminho, ip, db, dbf, porta):
    with open(caminho, encoding="cp1252") as arquivo:
        linhas = arquivo.readlines()
    linhas[0] = ip + "\n"
    linhas[1] = db + "\n"
    linhas[2] = dbf + "\n"
    linhas[3] = porta + "\n"
    with open(caminho, "w", encoding="cp1252") as arquivo:
        arquivo.writelines(linhas)

def alterar_conexao(ip, db, dbf, porta):
    alterar_arq(CONFIG_INI, ip, db, dbf, porta)
    alterar_arq(ENDERECO_INI, ip, db, dbf, porta)
    print("\n ----- Arquivos atualizados com sucesso -----\n")



def listar_executaveis_para_print(pasta, inicio):

    if inicio:
        padrao = f"WebCamara*{str(inicio)}*.EXE"
    else:
        padrao = "WebCamara*.EXE"

    executaveis = sorted(
        Path(pasta).glob(padrao),
        key=lambda arquivo: arquivo.stat().st_mtime,
        reverse=True
    )
    lista_EXE = [arquivo.name for arquivo in executaveis]
    versoes = []
    for item in lista_EXE:
        item = str(item).lower().replace('webcamara','').replace('.EXE','').strip()
        versoes.append(item)
    

    return versoes



def listar_Executaveis(pasta, sistema=None):

    if sistema:
        sistema = f"*{str(sistema)}*.EXE"
    else:
        sistema = "WebCamara*.EXE"

    executaveis = sorted(
        Path(pasta).glob(sistema),
        key=lambda arquivo: arquivo.stat().st_mtime,
        reverse=True
    )
    return executaveis


def procurar_ultimo_EXE(pasta, sistema=None):
    if sistema:
        lista = listar_Executaveis(pasta, sistema)
    else:
        lista = listar_Executaveis(pasta)

    if  len(lista) < 1:
        print("\nNenhum Executável encontrado.")
        return

    return lista[0]


def procurar_exe_manual(pasta):
    versao = input("\nVersão: ").replace(" ", "")
    versao = str(versao)
    if versao.count(".") == 0:
        versao = versao[0] + "." + versao[1:]
    numero = input("Executável: ").replace(" ", "")

    candidato = Path(pasta) / f"WebCamara {versao}({numero}).EXE"
    if candidato.exists():
        return candidato

    candidato = Path(pasta) / f"WebCamara {versao} ({numero}).EXE"
    if candidato.exists():
        return candidato
    
    if numero is None or numero == "":
        candidato = Path(pasta) / f"WebCamara {versao}.exe"
        if candidato.exists():
            return candidato 
    
    if int(numero) <= 1:
        candidato = Path(pasta) / f"WebCamara {versao}.exe"
        if candidato.exists():
            return candidato 
            
    print(alterar_cor("\nExecutável não encontrado.", "red", "sim")) # No caso de não encontrar NENHUM EXE parecido
    return None


def painel():

    LAST_ACCESS = BASE_DIR / "last_acess.txt"
    CORPADRAO = Config.CORPADRAO
    TAMANHOPADRAO = Config.TAMANHOPADRAO
    os.system(CORPADRAO)
    os.system(TAMANHOPADRAO)
    MINHAPASTA = Config.MINHAPASTA
    PASTACLIENTE = Config.PASTACLIENTE
    CONFIG_INI = Path(MINHAPASTA) / "configuracao.ini"
    ENDERECO_INI = Path(MINHAPASTA) / "endereco_ip_servidor.ini"
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
    print('           WebCamara CLIENTE                 DIGITE...        [4]                  ') 
    print('           Verificar Conexão atual            DIGITE...        [0]                  ') 
    print()
    print(alterar_cor('           Listar todos os EXE´s              DIGITE...        [E]                  ',"black", "sim")) 
    print(alterar_cor('           Rodar WebUpload                    DIGITE...        [W]                  ',"black", "sim"))
    print(alterar_cor('           Abrir última versão acessada       DIGITE...        [U]                  ',"yellow", "nao"))
    print()
    print(alterar_cor('====================================================================================',"cyan", "sim")) 


    RESPOSTA = input("\n> ")
    RESPOSTA = str(RESPOSTA).lower().strip()

    match RESPOSTA:
        case "1":
            alterar_conexao(IP,DB,DBF,PORTA)
            loading("Abrindo Versão mais recente do Homologação")
            time.sleep(2)
            EXE = (procurar_ultimo_EXE(MINHAPASTA))
            abrir_login(EXE)
            sys.exit()
        case "2":
            PERGUNTA = input(alterar_cor("\nDeseja escolher o Executável? [S/N]: ", "yellow", "nao")).strip().lower()
            match PERGUNTA:
                case "s":
                    EXE = procurar_exe_manual(MINHAPASTA)
                    if EXE:
                        alterar_arq(LAST_ACCESS, str(EXE), "", "Na linha acima esta o ultimo EXE aberto!", "")
                        abrir_login(EXE)
                    else:
                        pause()
                        painel()
                    sys.exit()
                case "n":
                    EXE = procurar_ultimo_EXE(MINHAPASTA)
                    alterar_arq(LAST_ACCESS, str(EXE), "", "Na linha acima esta o ultimo EXE aberto!", "")
                    abrir_login(EXE)
                    sys.exit()
                case _:
                    print(alterar_cor('\n -- RESPONDA SOMENTE "S" OU "N" --', 'red', 'sim'))
                    pause()
                    painel()
        case "3":
            cls()
            print(alterar_cor("\n======================== CONEXÃO PERSONALIZADA SELECIONADA =========================", "yellow", "nao"))
            print()
            IP = input("\n> IP: ").replace(" ","")
            PORTA = input("> PORTA: ").replace(" ","")
            DB = input("\n> BANCO REGISTROS: ").replace(" ","").lower()
            if "webcamara" not in DB:
                print(alterar_cor('\n Opa, parece que seu banco não começa com "webcamara", tem certeza?! \n', 'blue', 'sim'))
            DBF = input(alterar_cor("> BANCO ARQUIVOS: ", "yellow", "nao")).replace(" ","").lower()
            print()
            if IP == "" or PORTA == "" or DB == "" or DBF == "":
                print(alterar_cor("\n -- ALGUM CAMPO FICOU VAZIO! --", "red", "sim"))
                pause()
                painel()
            print()
            print("====================================================================================")
            alterar_conexao(IP,DB,DBF,PORTA)
            EXE = procurar_exe_manual(MINHAPASTA)
            alterar_arq(LAST_ACCESS, str(EXE), "", "Na linha acima esta o ultimo EXE aberto!", "")
            abrir_login(EXE)
            sys.exit()
        case "4":
            print()
            loading("Abrindo Versão mais recente de CLIENTE")
            EXE = procurar_ultimo_EXE(PASTACLIENTE)
            abrir_login(EXE)
            sys.exit()
        case "0":
            ip, db, dbf, porta = ver_conexao_atual(CONFIG_INI, 4)
            cls()
            os.system("color 0A")
            print()
            print("======================== CONEXÃO ATUAL DA SUA PASTA ABAIXO =========================")
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
                print("================== Defina a pasta em que deseja listar os EXE abaixo ===============")
                print()
                print("                  Minha Pasta                         DIGITE...    [1]")
                print("                  Pasta CLIENTE                      DIGITE...    [2]")
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
                        PASTASELECIONADA = MINHAPASTA
                        lista = listar_executaveis_para_print(PASTASELECIONADA,"")
                        for i in lista:
                            CONTADOR+=1
                        os.system(f"mode con: cols=87 lines={CONTADOR}")
                        break
                    case "2":
                        PASTASELECIONADA = PASTACLIENTE
                        lista = listar_executaveis_para_print(PASTASELECIONADA,"")
                        for i in lista:
                            CONTADOR+=1
                        os.system(f"mode con: cols=87 lines={CONTADOR}")
                        break
                    case "3":
                        SELECIONADA = input("\nDigite o caminho da pasta que deseja listar: ")
                        PASTASELECIONADA = SELECIONADA
                        lista = listar_executaveis_para_print(PASTASELECIONADA,"")
                        for i in lista:
                            CONTADOR+=1
                        os.system(f"mode con: cols=87 lines={CONTADOR}")
                        break
                    case "b":
                        PASTASELECIONADA = MINHAPASTA
                        inicio = input(alterar_cor("\nDigite os primeiros números da versão filtrada: ", "magenta", "sim"))
                        lista = listar_executaveis_para_print(PASTASELECIONADA, inicio)
                        for i in lista:
                            CONTADOR+=1
                        os.system(f"mode con: cols=87 lines={CONTADOR}")
                        break
                    case _:
                        pass
            CONTADOR = CONTADOR - 8
            TAMANHOMAX = 83
            if CONTADOR == 0:
                print(alterar_cor('\n\n======================= NENHUMA VERSÃO ENCONTRADA ! =======================', 'RED', 'sim'))
                pause()
                painel()
            else:
                print()
                TITULO = f' ({CONTADOR}) VERSÕES DISPONÍVEIS '
                TITULO = TITULO.center(TAMANHOMAX, "=")
                print(alterar_cor(TITULO, "green", "sim"))
                print()
                for versao in lista:
                    print(alterar_cor(f' ➤ {versao}', "cyan", "sim"))
                print()
                PASTASELECIONADA = (f" {PASTASELECIONADA} ").center(TAMANHOMAX, "=")
                print(alterar_cor(PASTASELECIONADA, "green", "sim"))
                input()
                painel()
        case "w":
            EXE = str(procurar_ultimo_EXE(MINHAPASTA, "Webupload"))
            print(f"\nCaminho encontrado: {EXE}")
            pause()
            somente_abrir_exe(EXE)
        case "u":
            print()
            loading(f"Reabrindo ultimo executável")
            EXE = ver_conexao_atual(LAST_ACCESS, 1)
            abrir_login(EXE)
        case _:
            painel()
painel()