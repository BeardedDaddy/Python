"""Optimize themes"""

import sys
import json
import time
from typing import List, Any, Dict  # pylint: disable=W0611

import requests

URL = 'https://raw.githubusercontent.com/MagicStack/MagicPython/master/misc/scopes'


class Pedle:
    pass


def main():
    """Main method"""
    console_args = sys.argv[1]

    with open(console_args, mode='r') as file:
        document = json.load(file)

    while True:
        try:
            possibles = requests.get(URL).text.split('\n')
            break
        except requests.exceptions.ConnectionError:
            print('Connection error retry..')
            time.sleep(1)

    elements = document['tokenColors']  # type: List[Dict]
    result = []  # type: List[Dict[str, Any]]

    for element in elements: # type: Dict[str, Any]
        scope, settings = element['scope'], element['settings']  # type: Any, Dict[str, str]
        foreground = settings.get('foreground')  # type: str

        if foreground:
            foreground = foreground.upper()

            if len(foreground) == 4:
                foreground += foreground[1:]
            elif not foreground and 'fontStyle' not in settings:
                continue
            elif len(foreground) == 9 and foreground[7:] == 'FF':
                foreground = foreground[:7]

            settings['foreground'] = foreground
        if 'fontStyle' not in settings:
            settings['fontStyle'] = ''

        if isinstance(scope, list):
            for current in scope:
                for token in current.split(' ').copy():
                    if not any(token in text for text in possibles):
                        print(f'Not in {token}')
                        scope.remove(current)
                        break
            result.append(element)
        elif isinstance(scope, str) and any(scope.strip() in text for text in possibles):
            result.append(element)
        else:
            print(f'Not in {scope}')

    document['tokenColors'] = result

    with open('output.json', mode='w') as file:
        json.dump(document, file, indent=4)


if __name__ == '__main__':
    main()
