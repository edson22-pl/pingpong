@echo off
powershell -Command "Invoke-WebRequest -Uri 'https://download.avica.com/AvicaLite_v8.0.8.9.exe' -OutFile Avica_setup.exe"
powershell -Command "Invoke-WebRequest -Uri 'https://telegram.org/dl/desktop/win64' -OutFile C:\Users\Public\Desktop\Telegram.exe"
powershell -Command "Invoke-WebRequest -Uri 'https://www.rarlab.com/rar/winrar-x64-621.exe' -OutFile C:\Users\Public\Desktop\Winrar.exe"
powershell -Command "Invoke-WebRequest -Uri 'https://gitlab.com/gusta7w7/pcrdp-avica/-/raw/main/wall.bat' -OutFile wall.bat"
powershell -Command "Invoke-WebRequest -Uri 'https://github.com/chieunhatnang/VM-QuickConfig/releases/download/1.6.1/VMQuickConfig.exe' -OutFile C:\Users\Public\Desktop\VMQuickConfig.exe"
python.exe -m pip install --upgrade pip
pip install requests --quiet
pip install pyautogui --quiet
pip install telegraph --quiet

C:\Users\Public\Desktop\Telegram.exe /VERYSILENT /NORESTART
del C:\Users\Public\Desktop\Telegram.exe
C:\Users\Public\Desktop\Winrar.exe /S
del C:\Users\Public\Desktop\Winrar.exe
del /f "C:\Users\Public\Desktop\Epic Games Launcher.lnk"
del /f "C:\Users\Public\Desktop\Unity Hub.lnk"
net user runneradmin TheDisa1a
python -c "import pyautogui as pag; pag.click(897, 64, duration=2)"
start "" "Avica_setup.exe"
python setup.py
call wall.bat
