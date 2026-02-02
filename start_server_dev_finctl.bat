@echo off
echo.
echo ========================================
echo   FINCTL - INICIANDO SERVIDOR DEV
echo ========================================
echo.

REM Navega para a pasta raiz do framework
cd /d "C:\Applications_DSB\framework_dsb"

REM Ativa o ambiente virtual
echo [1/3] Ativando ambiente virtual Python...
call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERRO: Falha ao ativar o ambiente virtual
    pause
    exit /b 1
)

REM Navega para a pasta do servidor e inicia
echo [2/3] Navegando para pasta do servidor...
cd backend\source_code

echo [3/3] Iniciando servidor FinCtl...
echo.
echo ⚡ Servidor será iniciado em: http://localhost:5000
echo ⚠️  Para parar o servidor: Ctrl+C
echo.
python server_Applications_DSB.py finctl

REM Se chegou aqui, o servidor foi interrompido
echo.
echo 🛑 Servidor interrompido
pause
