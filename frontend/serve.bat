@echo off
cd /d "%~dp0"
echo Starting static server at http://127.0.0.1:3000
python -m http.server 3000 --bind 127.0.0.1
pause
