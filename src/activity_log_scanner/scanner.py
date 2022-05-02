""" Allows for scanning of PNG images to extract activity log stats """
import cv2
import pytesseract
import re
import sys

if sys.platform.startswith('win32'):
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


KEYS = [
    'Enemy Player Damage',
    'Friendly Player Damage',
    'Enemy Structure/Vehicle Damage',
    'Friendly Structure/Vehicle Damage',
    'Friendly Construction',
    'Friendly Repairing',
    'Friendly Healing',
    'Friendly Revivals',
    'Vehicles Captured By Enemy',
    'Vehicle Self Damage',
    'Materials Submitted',
    'Materials Gathered',
    'Supply Value Delivered'
]


def scan(image):
    """ Scans an image """
    result = {}
    image_data = cv2.imread(image)
    image_text = pytesseract.image_to_string(image_data)
    for line in image_text.splitlines():
        if any(key in line for key in KEYS):
            kv = line.split(': ')
            result[re.sub(r'[\W_]+', '', kv[0]).strip()] = int(kv[1].replace(',', ''))
    for key in KEYS:
        result.setdefault(re.sub(r'[\W_]+', '', key).strip(), None)
    return result