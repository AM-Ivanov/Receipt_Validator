import os
import pdfplumber
import re
import barcode_validator
from flask import Flask, request
from uuid import uuid4
from test_params import fields_regexp, header_regexp, expected_page_count, header_reference, fields_list_reference, \
    wrong_page_count_error, unexpected_header_error, incorrect_fields_count_error, incorrect_fields_list_error, \
    no_content_error, incorrect_format_error

app = Flask(__name__)


@app.route('/validate_receipt', methods=['POST'])
def request_handler():
    # Request validation and saving file
    try:
        f = request.files['f']
    except:
        return no_content_error
    if f.filename[-4:] != '.pdf':
        return incorrect_format_error
    f_path = os.path.join("Test data/pdf", f'{uuid4()}{f.filename[-4:]}')
    f.save(f_path)
    return receipt_validator(f_path)


def receipt_validator(path):
    # File parsing
    receipt = pdfplumber.open(path)
    extracted_text = receipt.pages[0].extract_text()
    header = re.findall(header_regexp, extracted_text)[0]
    fields_list = re.findall(fields_regexp, extracted_text)
    fields_list_errors = incorrect_fields_list_error
    error_list = []
    # Validation
    if len(receipt.pages) != expected_page_count:
        error_list.append(f'{wrong_page_count_error}{len(receipt.pages)}')
    if header != header_reference:
        error_list.append(f'{unexpected_header_error}{header}')
    if len(fields_list_reference) == len(fields_list):
        for i in range(len(fields_list_reference)):
            if fields_list_reference[i] != fields_list[i]:
                fields_list_errors += f' {fields_list[i]},'
        if fields_list_errors != incorrect_fields_list_error:
            error_list.append(fields_list_errors)
    else:
        error_list.append(f'{incorrect_fields_count_error}{len(fields_list)}')
    error_list += barcode_validator.scan_and_validate(path)
    if len(error_list) > 0:
        return error_list
    else:
        return 'Checking header content -- passed\nChecking the list of fields -- passed\nChecking for barcodes -- passed'


if __name__ == '__main__':
    app.run(debug=True)
