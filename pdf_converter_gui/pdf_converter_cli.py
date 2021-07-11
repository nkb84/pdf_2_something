import click

from converter.pdf2html import Pdf2Html

arg = click.argument
opt = click.option


@click.command()
@opt('-o', '--output-folder', 'output_folder',
     required=True,
     type=click.Path(exists=True, file_okay=False),
     help='location to save the output')
@arg('pdf_file', type=click.Path(exists=True, dir_okay=False), )
def main(output_folder, pdf_file):
    converter = Pdf2Html(output_directory=output_folder, pdf_file=pdf_file)
    converter.convert()


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
