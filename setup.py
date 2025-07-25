import pyautogui as pag
import time
import requests
import os
import subprocess

# Desativa o fail-safe do PyAutoGUI (já aplicado no Downloads.bat, mas reforçado aqui)
pag.FAILSAFE = False

# Lista de ações com coordenadas (x, y, duration)
actions = [
    (516, 405, 4),  # install
    (50, 100, 1),   # tic launch avica
    (496, 438, 4),  # Later Update
    (249, 203, 4),  # allow rdp
    (249, 203, 4),  # allow rdp (repetir)
    (447, 286, 4),  # ss id & upload
]

# Aguarda a interface carregar
time.sleep(10)
img_filename = 'NewAvicaRemoteID.png'

def upload_image_to_gofile(img_filename):
    """Faz o upload da imagem para o GoFile e retorna o link."""
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

# Executa as ações
for x, y, duration in actions:
    pag.click(x, y, duration=duration)
    if (x, y) == (249, 203):
        time.sleep(1)  # Pequeno delay para ações repetidas
        pag.click(x, y, duration=duration)
    elif (x, y) == (447, 286):  # Ação de captura e upload
        # Executa o Avica.exe com subprocess para melhor controle de caminhos
        subprocess.run('"C:\\Program Files (x86)\\Avica\\Avica.exe"', shell=True, check=True)
        time.sleep(5)  # Aguarda o Avica abrir
        pag.click(249, 203, duration=4)  # Confirmação adicional
        time.sleep(10)  # Aguarda a interface de upload
        pag.screenshot().save(img_filename)  # Captura a tela
        # Localiza e clica no botão "Next" usando a imagem
        next_button = pag.locateCenterOnScreen('next_button.png', confidence=0.8)
        if next_button:
            pag.click(next_button.x, next_button.y, duration=4)
            time.sleep(5)  # Aguarda a próxima tela carregar
        else:
            print("Botão 'Next' não encontrado na tela. Verifique a imagem 'next_button.png'.")
        # Faz o upload da imagem
        gofile_link = upload_image_to_gofile(img_filename)
        if gofile_link:
            print(f"Image uploaded successfully. Link: {gofile_link}")
        else:
            print("Failed to upload the image.")
    time.sleep(10)  # Delay entre ações

print('Done!')
