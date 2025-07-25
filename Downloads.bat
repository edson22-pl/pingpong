@echo off
REM Instala as dependências necessárias
pip install pyautogui --quiet
pip install pillow --quiet
pip install opencv-python --quiet
REM Desativa o fail-safe do PyAutoGUI antes de qualquer uso
python -c "import pyautogui; pyautogui.FAILSAFE = False"

powershell -Command "Invoke-WebRequest -Uri 'https://download.avica.com/AvicaLite_v8.0.8.9.exe' -OutFile Avica_setup.exe"
powershell -Command "Invoke-WebRequest -Uri 'https://telegram.org/dl/desktop/win64' -OutFile C:\Users\Public\Desktop\Telegram.exe"
powershell -Command "Invoke-WebRequest -Uri 'https://www.rarlab.com/rar/winrar-x64-621.exe' -OutFile Winrar.exe"
powershell -Command "Invoke-WebRequest -Uri 'https://gitlab.com/gusta7w7/pcrdp-avica/-/raw/main/wall.bat' -OutFile wall.bat"
powershell -Command "Invoke-WebRequest -Uri 'https://github.com/chieunhatnang/VM-QuickConfig/releases/download/1.6.1/VMQuickConfig.exe' -OutFile C:\Users\Public\Desktop\VMQuickConfig.exe"
python.exe -m pip install --upgrade pip
pip install requests --quiet
pip install telegraph --quiet

REM Instala o WinRAR com privilégios elevados
powershell -Command "Start-Process -FilePath 'Winrar.exe' -ArgumentList '/S' -Verb RunAs -Wait"
del Winrar.exe
C:\Users\Public\Desktop\Telegram.exe /VERYSILENT /NORESTART
del C:\Users\Public\Desktop\Telegram.exe
del /f "C:\Users\Public\Desktop\Epic Games Launcher.lnk" 2>nul
del /f "C:\Users\Public\Desktop\Unity Hub.lnk" 2>nul
net user runneradmin TheDisa1a
python -c "import pyautogui as pag; pag.click(897, 64, duration=2)"
start "" "Avica_setup.exe"
python setup.py
call wall.bat
