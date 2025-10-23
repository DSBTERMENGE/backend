@echo off
echo Ativando ambiente conda sp1...
call conda activate sp1

echo Iniciando servidor Flask...
cd /d "C:\Applications_DSB\framework_dsb\backend"
python app.py

pause