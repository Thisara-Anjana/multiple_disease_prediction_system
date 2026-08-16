@echo off
setlocal

echo ===================================================
echo   Disease Prediction AI - Startup Script
echo ===================================================

echo [1/3] Checking dependencies...
where py >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    py -3.13 -m pip install -r requirements.txt
) else (
    python -m pip install -r requirements.txt
)

echo [2/3] Starting Backend Server...
echo The backend server will open in a new window. Do not close it!
where py >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    start "Disease Prediction Backend" py -3.13 -m uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
) else (
    start "Disease Prediction Backend" python -m uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
)

echo [3/3] Opening Frontend Interface...
timeout /t 3 >nul
start frontend/index.html

echo.
echo ===================================================
echo   System is running!
echo   - Backend: http://127.0.0.1:8000
echo   - Frontend: Opened in your browser
echo ===================================================
pause
endlocal
