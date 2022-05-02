""" Scans the provided image and appends it's data to a CSV """
import activity_log_scanner.scanner as scanner
import os
import sys

def xstr(s):
    if s is None:
        return ''
    return str(s)

def main():
    image = sys.argv[1]
    metadata, _ = os.path.basename(image).split('.')
    name, war = metadata.split('#')
    values = [name, int(war)]
    x = scanner.scan(image)
    x = {k: v for k, v in sorted(x.items(), key=lambda item: item[0])}
    values.extend(x.values())
    print(', '.join(['{}'.format(xstr(value)) for value in values]))