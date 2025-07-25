import pyautogui as pag
import time
import requests
import os

# Desativa o fail-safe do PyAutoGUI
pag.FAILSAFE = False

actions = [
    (516, 405, 4),  # install
    (50, 100, 1),   # tic launch avica
    (496, 438, 4),  # Later Update
    (249, 203, 4),  # allow rdp
    (249, 203, 4),  # allow rdp (repetir)
    (447, 286, 4),  # ss id & upload
]

time.sleep(10)
img_filename = 'NewAvicaRemoteID.png'

def upload_image_to_gofile(img_filename):
    url = 'https://store1.gofile.io/uploadFile'
    try:
        with open(img_filename, 'rb') as img_file:
            files = {'file': img_file}
            response = requests.post(url, files=files)
            response.raise_for_status()
            result = response.json()
            if result['status'] == 'ok':
                download_page = result['data']['downloadPage']
                with open('show.bat', 'a') as bat_file:
                    bat_file.write(f'\necho Avica Remote ID : {download_page}')
                return download_page
            else:
                print("Upload error:", result.get('status'))
                return None
    except Exception as e:
        print(f"Failed to upload image: {e}")
        return None

for x, y, duration in actions:
    pag.click(x, y, duration=duration)
    if (x, y) == (249, 203):
        time.sleep(1)
        pag.click(x, y, duration=duration)
    if (x, y) == (447, 286):
        # Corrige a sintaxe para executar o Avica.exe com caminho correto
        os.system('"C:\\Program Files (x86)\\Avica\\Avica.exe"')
        time.sleep(5)
        pag.click(249, 203, duration=4)
        time.sleep(10)
        pag.screenshot().save(img_filename)
        gofile_link = upload_image_to_gofile(img_filename)
        if gofile_link:
            print(f"Image uploaded successfully. Link: {gofile_link}")
        else:
            print("Failed to upload the image.")
    time.sleep(10)

print('Done!')
