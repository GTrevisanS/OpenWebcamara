:RECENTEXE

set "PYEXE="

for /f "delims=" %%i in ('dir /b /a-d /o-d "%~1\*.exe"') do (

    set "PYEXE=%~1\%%i"

    goto :FIM_RECENTEXE
)

echo.
echo Nenhum EXE encontrado.
echo.

exit /b


:FIM_RECENTEXE

echo ------------------------------------------------------------
echo    EXE ENCONTRADO:
echo.
echo    %PYEXE%
echo ------------------------------------------------------------
echo.

exit /b