Preconditions:
- Installed following modules by pip: pip install pdfplumber flask pyzbar numpy Pillow pdf2image
- Installed latest poppler: https://github.com/oschwartz10612/poppler-windows/releases/
- Written path to poppler/Library/bin in barcode_validator.py > def convertation_to_img > argument poppler_path

Some description of the API method:
- Route: /validate_receipt
- Method: POST
- Body:
    Content Type: multipart/form-data
    Parameter name: f
    Data: pdf file
- Example: 
curl --location 'http://<ip or domain name>/validate_receipt' \
--form 'f=@"<path to file>"'

What can the method do:
- Checking that request contains right content (including file format)
- Checking texts in document (including header text, number of document fields, their naming and order)
- Checking barcodes (including their count, their type and positions in document)

If all tests are passed method returns following response:
Checking header content -- passed
Checking the list of fields -- passed
Checking of barcodes -- passed

Else returns list of errors.