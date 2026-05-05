:: For this script to work, it must be run with administrator privileges
:: otherwise, error may occur during the installation of the requirements

@echo off
title Suomi Setup

python --version >nul 2>&1

if errorlevel 1 (
color 0A
echo Error: No Python installed, you need at least Python 3.14 to continue.
pause
exit /b
)

for /f "tokens=2 delims= " %%i in ('python --version') do set PYVER=%%i
echo %PYVER% | findstr /r "^3.14" >nul

if errorlevel 1 (
echo Error: Incorrect Python version, 3.14 is required.
exit /b
)

if not exist venv python -m venv .venv
call .venv\Scripts\activate

echo Suomi: Installing requirements.txt
pip install --upgrade pip
pip install -r requirements.txt

echo Suomi: Running shot.py
python shot.py

pause