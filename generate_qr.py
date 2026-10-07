import importlib.util
import subprocess
import sys

url = 'https://raizenpain.github.io/CSO-NATUREAQUARIUM/'
out_path = r'd:\Aquarium\qrcode.png'

spec = importlib.util.find_spec('qrcode')
if spec is None:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'qrcode[pil]'])

import qrcode
img = qrcode.make(url)
img.save(out_path)
print(f'Created QR code: {out_path}')
