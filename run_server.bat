@echo off
set file=server\server.py

REM Check if the Python file exists
if exist "%file%" (
    REM Check if Python is installed and in the PATH
    python --version >nul 2>&1
    if errorlevel 1 (
        echo Python is not installed or not found in PATH.
    ) else (
        REM Run the Python file
        python "%file%"
    )
) else (
    echo File not found: %file%
)
