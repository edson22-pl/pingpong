@echo off
REM Instala o pyautogui antes de usá-lo
pip install pyautogui --quiet
REM Desativa o fail-safe do PyAutoGUI
python -c "import pyautogui; pyautogui.FAILSAFE = False"

start "" /MAX "C:\Users\Public\Desktop\VMQuickConfig.exe"
python -c "import pyautogui as pag; pag.click(143, 487, duration=5)"
python -c "import pyautogui as pag; pag.click(155, 554, duration=2)"
python -c "import pyautogui as pag; pag.click(637, 417, duration=2)"
python -c "import pyautogui as pag; pag.click(588, 10, duration=2)"

echo Telegram: https://t.me/TheDisala4U
echo Created by a Brazilian
echo By abelha7w7
echo Method Fixed 2025!!!

echo User name : runneradmin
echo User Pass : TheDisa1a

echo Chupa Gitlab de Merda!
