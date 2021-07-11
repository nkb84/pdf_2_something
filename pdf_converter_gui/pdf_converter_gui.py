from gooey import Gooey, GooeyParser

from converter.pdf2html import Pdf2Html


def list_output_types():
    return [
        "html",
    ]


@Gooey(program_name='PDF converter')
def main():
    settings_msg = 'This program will convert pdf file to docx or pptx'
    parser = GooeyParser(description=settings_msg)
    required_group = parser.add_argument_group('Required arguments')
    required_group.add_argument(
        '--pdf-file',
        help="Source pdf file",
        dest='pdf_file',
        action='store',
        widget='FileChooser', )

    required_group.add_argument(
        '--type',
        help='Define the output file type',
        dest='output_type',
        widget='Dropdown',
        choices=list_output_types(),
        default=list_output_types()[0],
    )
    required_group.add_argument(
        '--out-folder',
        help='Output folder',
        dest='out_folder',
        widget='DirChooser')

    args = parser.parse_args()
    if args.output_type == 'html':
        converter = Pdf2Html(pdf_file=args.pdf_file, output_directory=args.out_folder)
        converter.convert()
        print(f"Output file is {converter.get_output_file()}")
    else:
        print(f"We have not yet supported the type {args.output_type}")


if __name__ == '__main__':
    main()
