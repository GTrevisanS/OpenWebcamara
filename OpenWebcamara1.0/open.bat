@echo off
setlocal
color 5F 
echo.
type banner.txt 
echo.
timeout /t 2 /nobreak >nul
:return
cls
echo.

set VERSAO=
set EXECUTÁVEL=
set IP=
set DB=
set DBF=
set PORTA=

echo ===========================================================================
echo.
echo           Defina os parametros abaixo para entrar no programa.
echo.
echo            (escreveu algo errado?, digite "x" para reiniciar)
echo.
echo ===========================================================================

echo.
echo    Deixe tudo em branco caso queira acessar o ultimo EXE:
echo.

set /p VERSAO=Digite a versao do webcamara: 
if /i "%VERSAO%"=="x" goto return
set /p EXECUTAVEL=Digite o numero do executavel: 
if /i "%EXECUTAVEL%"=="x" goto return

echo.
echo    Deixe tudo em branco caso queira acessar o webcamara de homologacao:
echo.

set /p IP=Digite o IP: 
if /i "%IP%"=="x" goto return
set /p DB=Digite o nome do Banco: 
if /i "%DB%"=="x" goto return
set /p DBF=Digite o nome do banco de arquivos: 
if /i "%DBF%"=="x" goto return
set /p PORTA=Digite a Porta: 
if /i "%PORTA%"=="x" goto return

:: Abaixo ficaria a conexao padrao do servidor e banco da empresa
:: Removi por questoes de sensibilidade / seguranca

if /i "%IP%"=="" set "IP="
if /i "%DB%"=="" set "DB="
if /i "%DBF%"=="" set "DBF="
if /i "%PORTA%"=="" set "PORTA="

powershell -NoProfile -ExecutionPolicy Bypass -Command "$ErrorActionPreference='Stop'; try { $arquivo='C:\Webline\MinhaPasta\configuracao.ini'; $c=[System.IO.File]::ReadAllLines($arquivo, [System.Text.Encoding]::Default); $c[0]='%IP%'; $c[1]='%DB%'; $c[2]='%DBF%'; $c[3]='%PORTA%'; [System.IO.File]::WriteAllLines($arquivo, $c, [System.Text.Encoding]::Default); Write-Host ''; Write-Host 'SUCESSO'; } catch { Write-Host ''; Write-Host '===================='; Write-Host 'ERRO:'; Write-Host $_.Exception.Message; Write-Host '===================='; pause; exit 1; }"
powershell -NoProfile -ExecutionPolicy Bypass -Command "$ErrorActionPreference='Stop'; try { $arquivo='C:\Webline\MinhaPasta\endereco_ip_servidor.ini'; $c=[System.IO.File]::ReadAllLines($arquivo, [System.Text.Encoding]::Default); $c[0]='%IP%'; $c[1]='%DB%'; $c[2]='%DBF%'; $c[3]='%PORTA%'; [System.IO.File]::WriteAllLines($arquivo, $c, [System.Text.Encoding]::Default); Write-Host 'SUCESSO'; } catch { Write-Host ''; Write-Host '===================='; Write-Host 'ERRO:'; Write-Host $_.Exception.Message; Write-Host '===================='; pause; exit 1; }"

if %errorlevel% neq 0 (
    echo.
    echo O SCRIPT FALHOU.
    pause
    exit /b
)

if /i "%EXECUTAVEL%"=="%VERSAO%" goto lastEXE

echo.
echo =========================
echo    ABRINDO WEBCAMARA...
echo =========================
echo.
set "EXE=WebCamara %VERSAO% (%EXECUTAVEL%).exe"
:found
echo.
echo Executando: %EXE%
start "" "C:\Webline\MinhaPasta\%EXE%"
echo.
timeout /t 2 /nobreak >nul
exit

:lastEXE
echo.
echo PROCURANDO VERSAO MAIS RECENTE...
timeout /t 1 /nobreak >nul
for /f "delims=" %%i in ('dir /b /a-d /o-d "C:\Webline\MinhaPasta\*.exe"') do (
    set "EXE=%%i"
    goto found
)