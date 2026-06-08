@echo off
title MovieSearch MySQL Demo

cd /d "%~dp0"

echo ===================================================
echo   Starting MovieSearch MySQL Demo...
echo ===================================================

if not exist "venv\Scripts\python.exe" (
    echo ERROR: Virtual environment not found.
    echo Create it first:
    echo python -m venv venv
    echo venv\Scripts\activate
    echo python -m pip install -r backend\requirements.txt
    pause
    exit /b
)

echo Starting FastAPI server...
start "MovieSearch MySQL Server" cmd /k "venv\Scripts\python.exe -m uvicorn main:app --host 127.0.0.1 --port 8000"

echo Waiting for server to start...
timeout /t 8 /nobreak > nul

echo Opening Swagger documentation...
start "" "http://127.0.0.1:8000/docs"

echo Opening frontend page...
start "" "%~dp0frontend\index.html"

echo.
echo Demo started successfully!
echo.
pause