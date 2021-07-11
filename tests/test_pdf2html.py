import os
from pathlib import Path

import pytest

from converter.pdf2html import Pdf2Html


@pytest.fixture
def pdf2html(request):
    converter = Pdf2Html(pdf_file=request.param,
                   output_directory=".")
    yield converter
    os.remove(converter.get_output_file())



def content_of(file_path):
    with open(file_path, 'r') as input_file:
        return input_file.read()


@pytest.mark.parametrize(
    'pdf2html',
    [
        r"data\Financial Plan Checklist.pdf",
        r"data\N2-script-nghe.pdf",
        r"data\Party Planning Checklist.pdf",
    ],
    indirect=True
)
def test_convert_pdf2html(pdf2html: Pdf2Html):
    pdf2html.convert()
    html_output_file = pdf2html.get_output_file()
    assert Path(html_output_file).exists()
    assert 'id="page' in content_of(html_output_file)
    assert '<img ' in content_of(html_output_file)
