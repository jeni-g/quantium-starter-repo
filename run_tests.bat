@echo off

call venv311\Scripts\activate

pytest

IF %ERRORLEVEL% EQU 0 (
    echo All tests passed
    exit /b 0
) ELSE (
    echo Tests failed
    exit /b 1
)