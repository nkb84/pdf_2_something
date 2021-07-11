import fitz
from fitz import fitz
from tqdm import trange

from converter.pdf_converter import PdfConverter


class Pdf2Html(PdfConverter):
    def _get_suffix(self):
        return '.html'

    def convert(self):
        doc = fitz.open(self.pdf_file)
        print(self.pdf_file, 'contains', doc.pageCount, 'slides')
        html_data = ""
        page_count = doc.pageCount
        for page_no in trange(0, page_count):
            page = doc.loadPage(page_no)
            html = self._generate_html_for_one_page(page)
            html = html.replace('</div>', f'<p>Page {page.number + 1}/{page_count}</p></div>')
            html_data += html

        html_page = self._generate_html_doc(html_data)
        with open(self.output_file, 'w') as output_file:
            output_file.write(html_page)

    def _generate_html_doc(self, html_data):
        header = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>
        <div>
        """
        footer = """
        </div>
        </body>
        </html>
        """
        return header + html_data + footer

    def _generate_html_for_one_page(self, page):
        styles = [
            "position:relative",
            "border: 1px solid black",
            "margin: auto",
        ]

        html = page.get_text('html')
        html = html.replace(
            'style="position:relative',
            f'style="{";".join(styles)};')
        html = html.replace('id="page0"', f'id="page{page.number}"')
        return html
