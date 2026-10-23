import importlib.util
import os
import subprocess
import sys

url = 'https://raizenpain.github.io/CSO-NATUREAQUARIUM/'
out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'qrcode.png')

spec = importlib.util.find_spec('qrcode')
if spec is None:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'qrcode[pil]'])

import qrcode
img = qrcode.make(url)
img.save(out_path)
print(f'Created QR code: {out_path}')
