# Test config
header_regexp = r'[\s\w\s]+\n'
fields_regexp = r'[A-Z-a-z-]+[\s]*[:]\s'
expected_page_count = 1
header_reference = 'GRIFFON AVIATION SERVICES LLC\n'
fields_list_reference = ['PN: ', 'SN: ', 'DESCRIPTION: ', 'LOCATION: ', 'CONDITION: ', 'UOM: ', 'DATE: ', 'PO: ',
                         'SOURCE: ', 'DATE: ', 'MFG: ', 'DOM: ', 'REMARK: ', 'BY: ', 'NOTES:\n', 'Qty: ']
expected_barcode_count = 2
expected_barcode_type = 'CODE128'
expected_barcode_indents = [[56, 430], [38, 50]]  # [left, top]
successful_response = 'Checking header content -- passed\nChecking the list of fields -- passed\nChecking of barcodes -- passed'
# Request validation error texts
no_content_error = 'RequestValidationError: Request has to contain a PDF file.'
incorrect_format_error = 'RequestValidationError: File has another format then PDF.'
# File validation error texts
unexpected_header_error = f'Unexpected receipt header. Expected: {header_reference}'
unexpected_fields_list_error = f'Unexpected list of receipt fields. Expected: {fields_list_reference}'
wrong_page_count_error = f'Expected number of pages {expected_page_count} but actually '
barcode_errors = {'wrong_count': f'Barcode Validation failed: Wrong count of the barcodes in file. Expected {expected_barcode_count} but actually ',
                  'wrong_type': f'Wrong type of the barcode №',
                  'wrong_position': 'Unexpected position of the barcode №'}
