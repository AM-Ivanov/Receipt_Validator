from pyzbar import pyzbar
from numpy import asarray
from PIL import Image
from pdf2image import convert_from_path
from uuid import uuid4
from test_params import expected_barcode_type, expected_barcode_count, expected_barcode_indents, barcode_errors
import os


def scan_and_validate(pdf_path):
    img_path = convertation_to_img(pdf_path)
    img = Image.open(img_path)
    img_numpydata = asarray(img)
    # Decodes all barcodes from an image
    decoded_objects = pyzbar.decode(img_numpydata)
    # Barcode validation
    error_list = []
    if len(decoded_objects) != expected_barcode_count:
        error_list.append(f"{barcode_errors['wrong_count']}{len(decoded_objects)}")
        return error_list
    else:
        for i in range(len(decoded_objects)):
            if decoded_objects[i].type != expected_barcode_type:
                error_list.append(f"{barcode_errors['wrong_type']}{2 - i}")
            if decoded_objects[i].rect.left != expected_barcode_indents[i][0] or decoded_objects[i].rect.top != \
                    expected_barcode_indents[i][1]:
                error_list.append(f"{barcode_errors['wrong_position']}{2 - i}")
    return error_list


def convertation_to_img(path):
    images = convert_from_path(path, poppler_path='C:\\Program Files\\poppler-23.07.0\\Library\\bin')
    img_path = os.path.join("Test data/img", f'{uuid4()}.png')
    images[0].save(img_path)
    return img_path
