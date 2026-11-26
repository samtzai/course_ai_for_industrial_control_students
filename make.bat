@echo off
REM Windows batch file equivalent to Makefile
REM Usage: make.bat <target> [args]
REM Available targets: install, train, format, lint, git-config

if "%1"=="" (
    echo Available targets:
    echo   install    - Install dependencies and set up project
    echo   train      - Train the model
    echo   format     - Format code with ruff
    echo   lint       - Lint code with ruff
    echo   git-config - Configure git name, email and merge strategy
    echo                Usage: make.bat git-config "Your Name" "your@email.com"
    echo.
    echo Usage: make.bat ^<target^>
    goto :eof
)

if "%1"=="install" goto install
if "%1"=="train" goto train
if "%1"=="format" goto format
if "%1"=="lint" goto lint
if "%1"=="git-config" goto git-config

echo Error: Unknown target "%1"
echo Run "make.bat" without arguments to see available targets
goto :eof

:install
uv sync
echo.
echo ------------------ PROJECT READY ----------------------
echo Activate env: .venv\Scripts\activate
echo Train model: make.bat train
echo.
goto :eof

:git-config
if "%~2"=="" goto git-config-usage
if "%~3"=="" goto git-config-usage
git config --global user.name "%~2"
git config --global user.email "%~3"
git config --global pull.rebase false
git config --global pull.ff false
echo.
echo ------------------ GIT CONFIGURED ---------------------
echo user.name:  %~2
echo user.email: %~3
echo pull strategy: merge (no rebase, no fast-forward)
echo.
goto :eof

:git-config-usage
echo Error: git-config requires your name and email
echo Usage: make.bat git-config "Your Name" "your@email.com"
goto :eof

:train
python -m src.train
goto :eof

:format
ruff src
goto :eof

:lint
ruff check src
goto :eof