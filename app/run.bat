@echo off
REM Script de inicio rápido para AIRA
REM ============================================================

echo.
echo ========================================
echo   AIRA - IA en Salud Europa
echo   Iniciando aplicacion...
echo ========================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no esta instalado o no esta en el PATH
    echo Por favor, instala Python 3.8 o superior desde https://www.python.org/
    pause
    exit /b 1
)

echo [1/3] Verificando Python... OK
echo.

REM Verificar si las dependencias están instaladas
python -c "import streamlit" >nul 2>&1
if errorlevel 1 (
    echo [2/3] Instalando dependencias...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: No se pudieron instalar las dependencias
        pause
        exit /b 1
    )
) else (
    echo [2/3] Dependencias instaladas... OK
)
echo.

REM Iniciar la aplicación
echo [3/3] Iniciando Streamlit...
echo.
echo La aplicacion se abrira automaticamente en tu navegador
echo URL: http://localhost:8501
echo.
echo Presiona Ctrl+C para detener la aplicacion
echo.

streamlit run app.py

pause
