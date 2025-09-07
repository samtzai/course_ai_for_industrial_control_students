# PowerShell script to create and setup virtual environment

# Uncomment to install SWIG in Windows
# winget install --id=SWIGWin.SWIG -e

Write-Host "Creating virtual environment..." -ForegroundColor Green
python -m venv env

if ($LASTEXITCODE -ne 0) {
    Write-Host "Failed to create virtual environment. If it did not exist, try running as Administrator." -ForegroundColor Red
    Read-Host "Press Enter to continue..."
    exit 1
}

Write-Host "Activating environment..." -ForegroundColor Green
if (Test-Path "env\Scripts\Activate.ps1") {
    & ".\env\Scripts\Activate.ps1"
} else {
    Write-Host "Virtual environment activation script not found!" -ForegroundColor Red
    Read-Host "Press Enter to continue..."
    exit 1
}

Write-Host "Updating pip..." -ForegroundColor Green
python -m pip install --upgrade pip

Write-Host "Installing requirements..." -ForegroundColor Green
python -m pip install -e .[dev]

Write-Host "Environment setup complete!" -ForegroundColor Green
# python -m pip install box2D
Write-Host "activate your environment with '.\env\Scripts\Activate.ps1'" -ForegroundColor Yellow
