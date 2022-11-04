"""
Learning how to check the hash of a file.
"""

import hashlib

PUBLISHED_HASH = '4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6'

FILENAME = 'colorama-0.4.6-py2.py3-none-any.whl'

with open(FILENAME, 'rb') as downloaded_file:
    contents = downloaded_file.read()

FILE_HASH = hashlib.sha256(contents).hexdigest()
print(FILE_HASH)

if FILE_HASH != PUBLISHED_HASH:
    print(f'The file {FILENAME} has been modified')
else:
    print(f'The file {FILENAME} hash is correct')
