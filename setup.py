import os
import sys
import subprocess

plugin_dir = os.path.dirname(__file__)
gfpgan_dir = os.path.join(plugin_dir, 'gfpgan')
weights_dir = os.path.join(gfpgan_dir, 'weights')

def setup():
    download_weights()
    install_requirements()
    append_python_paths()

def download_weights():
    if not os.path.exists(weights_dir):
        os.makedirs(weights_dir)

    weights = [
            {
                'name': 'GFPGANv1.3.pth',
                'url': 'https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.3.pth',
            },
            {
                'name': 'GFPGANv1.4.pth',
                'url': 'https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth',
            },
            {
                'name': 'RestoreFormer.pth',
                'url': 'https://github.com/TencentARC/GFPGAN/releases/download/v1.3.4/RestoreFormer.pth',
            }
        ]

    for weight in weights:
        weight_url = weight['url']
        weight_path = os.path.join(weights_dir, weight['name'])

        if not os.path.exists(weight_path):
            os.system(f'wget {weight_url} -O {weight_path}')

def install_requirements():
    requirements_path = os.path.join(plugin_dir, 'requirements.txt')
    out = subprocess.check_output(['pip', 'install', '-r', requirements_path])

    for line in out.splitlines():
        print(line)
        
def append_python_paths():
    if plugin_dir not in sys.path:
        sys.path.append(plugin_dir)

    if gfpgan_dir not in sys.path:
        sys.path.append(gfpgan_dir)
