from zipfile import ZipFile
import os

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from __competition__ import COMP_NAME

if __name__ == '__main__':
    print(f'kaggle competition name: {COMP_NAME}\n')
    print('files found: ')
    os.system(f'kaggle competitions files {COMP_NAME}')
    print('\ndownloading...')
    os.system(f'kaggle competitions download {COMP_NAME}')

    filename = f'{COMP_NAME}.zip'
    print('extracting into localdata/')
    with ZipFile(filename, 'r') as zipf:
        zipf.extractall('localdata')
    os.remove(filename)
