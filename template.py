import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='[%s(asctime)s]: %(message)s:')

list_of_files = [
    'src/_init_.py',
    'src/run_local.py',
    'src/helper.py',
    'model/instruction.py',
    'requirements.txt',
    'setup.py',
    'main.py',
    'research/trials.ipynb',

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != '':
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f'File created: {filepath}')
    else:
        logging.info(f'File already exists: {filepath}')
