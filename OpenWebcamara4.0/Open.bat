@echo off
setlocal EnableDelayedExpansion

call Config.bat
call Predefinitions.bat

:: Abaixo fica o banner inicial "OpenWebcamara"
python Banner.py

set /a N=0
for /f "delims=" %%A in (%MINHAPASTA%\configuracao.ini) do (
    set /a N+=1

    if !N!==1 set "IPATUAL=%%A"
    if !N!==2 set "DBATUAL=%%A"
    if !N!==3 set "DBFATUAL=%%A"
    if !N!==4 set "PORTAATUAL=%%A"
)


:: ---------------------------------------------------------------- Painel inicial
:PAINEL
mode con: cols=87 lines=22
cls
echo.
echo =============================================================================
echo.
echo           DEFINA QUE TIPO DE ACAO VOCE DESEJA REALIZAR PELO PAINEL:
echo.
echo            WebCamara Homologacao              DIGITE...        [1]
echo            Conexao Rapida (Apenas abrir)      DIGITE...        [2]
echo            Conexao Personalizada              DIGITE...        [3]
echo            WebCamara Prudente                 DIGITE...        [4]
echo            Verificar Conexao atual            DIGITE...        [0]
echo.
echo            Rodar WebUpload                    DIGITE...        [W]
echo            Listar todos os EXE                DIGITE...        [E]
echo.
echo =============================================================================
echo.
set /p RESPOSTA=
if /i "%RESPOSTA%" =="" goto PAINEL
if /i "%RESPOSTA%" =="1" goto HOMOLOGACAO
if /i "%RESPOSTA%" =="2" goto FLASH
if /i "%RESPOSTA%" == "3" goto PERSONA
if /i "%RESPOSTA%" == "4" goto PRUDENTE
if /i "%RESPOSTA%" == "0" goto ATUALCONEX
if /i "%RESPOSTA%" == "W" goto WEBUPLOAD
if /i "%RESPOSTA%" == "E" goto SHOW
if /i "%RESPOSTA%" == "." goto CREDITOS
if /i "%RESPOSTA%" == "sair" exit
else goto :PAINEL
:: ------------------------------------------------------------------------------











:: -------------------------------------------------------- WebCamara Homologacao 
:HOMOLOGACAO
set "RETORNO=HOM"
cls
echo.
echo =============================================================================
echo.
echo                     WebCamara Homologacao selecionado!
echo.
echo                            ABRINDO WEBCAMARA...
echo.
echo =============================================================================
echo.
timeout /t 2 /nobreak >nul
goto CONECTAR
:HOM
call SearchEXE.bat %MINHAPASTA%
Goto FINAL
exit
:: ------------------------------------------------------------------------------










::-------------------------------------------------------------- Conexao Rapida
:FLASH
set "RETORNO=FLA"
echo.
set /p PERGUNTA=Deseja escolher a versao e o executavel? [S/N]: 

if /i "%PERGUNTA%"=="s" goto Escolher

if /i "%PERGUNTA%"=="N" call SearchEXE.bat %MINHAPASTA%
Goto FINAL
exit


:Escolher
set /p VERSAO=Digite a versao do webcamara: 
set /p EXECUTAVEL=Digite o numero do executavel: 
echo.
timeout /t 1 /nobreak >nul

:FLA
set "PYEXE=%MINHAPASTA%\WebCamara %VERSAO%(%EXECUTAVEL%).exe"
Goto FINAL
exit
:: ----------------------------------------------------------------------------











::-------------------------------------------------------- Conexao Personalizada 
:PERSONA
echo.
set "RETORNO=PERS"
set /p VERSAO=Digite a versao do webcamara: 
set /p EXECUTAVEL=Digite o numero do executavel: 
echo.
set /p IP=Digite o IP: 
set /p DB=Digite o nome do Banco: 
set /p DBF=Digite o nome do banco de arquivos: 
set /p PORTA=Digite a Porta: 
goto CONECTAR
:PERS
set "PYEXE=%MINHAPASTA%\WebCamara %VERSAO%(%EXECUTAVEL%).exe"
Goto FINAL
exit
:: ----------------------------------------------------------------------------











:: ---------------------------------------------------------- Webcamara Prudente
:PRUDENTE
cls
color 06
echo.
echo =============================================================================
echo.
echo                       WebCamara Prudente selecionado!
echo.
echo                            ABRINDO WEBCAMARA...
echo.
echo =============================================================================
echo.
timeout /t 2 /nobreak >nul
call SearchEXE.bat %PASTAPRUDENTE%
timeout /t 2 /nobreak >nul
Goto FINAL
exit
:: ----------------------------------------------------------------------------











:: -------------------------------------------------------- Checar Conexao Atual
:ATUALCONEX
cls
echo.
echo =============================================================================
echo.
echo                          Sua conexao atual da pasta:
echo.
echo              IP: %IPATUAL%
echo              DB: %DBATUAL%
echo              DB2: %DBFATUAL%
echo              Porta: %PORTAATUAL%
echo.
echo.
echo       Dados sendo coletados de: "%MINHAPASTA%"
echo.
echo =============================================================================
echo.
echo.
echo.
pause
goto PAINEL
:: ----------------------------------------------------------------------------











:: ------------------------------------------------------------ Rodar WebUpload
:WEBUPLOAD
echo.
echo Abrindo WebUpload...
timeout /t 2 /nobreak >nul
start "" "%MINHAPASTA%\Webupload 3.041(6).exe"
timeout /t 2 /nobreak >nul
exit
:: ---------------------------------------------------------------------------












:: ------------------------------------------------------------ Mostrar EXE´s
:SHOW
cls
mode con: cols=87 lines=5000
echo.
echo =============================================================================
echo.
echo              [Defina a pasta em que deseja listar os EXE abaixo]
echo.
echo               Minha Pasta              DIGITE...            [1]
echo               Pasta Prudente           DIGITE...            [2]
echo               Pasta Personalizada      DIGITE...            [3]
echo.
echo =============================================================================
echo.
set /p RESPOSTA= 
if /i "%RESPOSTA%" =="1" goto PPADRAO
if /i "%RESPOSTA%" =="2" goto PPRUDENTE
if /i "%RESPOSTA%" =="3" goto PPERSONAL


:PPRUDENTE
echo.
for /f "delims=" %%i in ('dir /b /a-d /o-d "%PASTAPRUDENTE%\webcamara*.exe"') do (
    echo %%i
)
echo.
pause
goto PAINEL



:PPADRAO
echo.
for /f "delims=" %%i in ('dir /b /a-d /o-d "%MINHAPASTA%\webcamara*.exe"') do (
    echo %%i
)
echo.
pause
goto PAINEL



:PPERSONAL
echo.
set /p PASTAESCOLHIDA=Defina o caminho da pasta onde estao os EXE: 
echo.
for /f "delims=" %%i in ('dir /b /a-d /o-d "%PASTAESCOLHIDA%\webcamara*.exe"') do (
    echo %%i
)
echo.
pause
goto PAINEL



:: ---------------------------------------------------------------------------











:: ------------------------------------------------------------------------------ FUNCAO QUE ALTERA OS TXT ------------------------------------------------------------------------------



:CONECTAR
powershell -NoProfile -ExecutionPolicy Bypass -Command "$ErrorActionPreference='Stop'; try { $arquivo='%MINHAPASTA%\configuracao.ini'; $c=[System.IO.File]::ReadAllLines($arquivo, [System.Text.Encoding]::Default); $c[0]='%IP%'; $c[1]='%DB%'; $c[2]='%DBF%'; $c[3]='%PORTA%'; [System.IO.File]::WriteAllLines($arquivo, $c, [System.Text.Encoding]::Default); Write-Host ''; Write-Host 'SUCESSO'; } catch { Write-Host ''; Write-Host '===================='; Write-Host 'ERRO:'; Write-Host $_.Exception.Message; Write-Host '===================='; pause; exit 1; }"
powershell -NoProfile -ExecutionPolicy Bypass -Command "$ErrorActionPreference='Stop'; try { $arquivo='%MINHAPASTA%\endereco_ip_servidor.ini'; $c=[System.IO.File]::ReadAllLines($arquivo, [System.Text.Encoding]::Default); $c[0]='%IP%'; $c[1]='%DB%'; $c[2]='%DBF%'; $c[3]='%PORTA%'; [System.IO.File]::WriteAllLines($arquivo, $c, [System.Text.Encoding]::Default); Write-Host 'SUCESSO'; } catch { Write-Host ''; Write-Host '===================='; Write-Host 'ERRO:'; Write-Host $_.Exception.Message; Write-Host '===================='; pause; exit 1; }"
echo.
echo ARQUIVOS ATUALIZADOS.
echo.
goto %RETORNO%
timeout /t 1 /nobreak >nul





:: ---------------------------------------------------------------------------- PYTHON QUE ABRE O WEBCAMARA ----------------------------------------------------------------------------- 


:FINAL
echo.
python Login.py "%PYUSUARIO%" "%PYSENHA%" "%PYEXE%"
goto PAINEL





:: --------------------------------------------------------------------------------------- CREDITOS ---------------------------------------------------------------------------------------

:CREDITOS
cls
type Frames\Credit.txt
pause
goto PAINEL




