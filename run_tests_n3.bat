@echo off
cd /d %~dp0
echo Running tests in 1 thread...
.venv\Scripts\python.exe -m pytest -v -n 3
echo.
echo Generating Allure report...
allure serve allure-results
pause