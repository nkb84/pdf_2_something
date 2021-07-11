import os
from abc import abstractmethod
from pathlib import Path


class PdfConverter:
    def __init__(self, pdf_file, output_directory):
        self.output_file = Path(output_directory).joinpath(os.path.basename(pdf_file)).with_suffix(self._get_suffix())
        self.pdf_file = pdf_file

    @abstractmethod
    def convert(self):
        pass

    @abstractmethod
    def _get_suffix(self):
        pass

    def get_output_file(self):
        return self.output_file
