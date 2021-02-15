from pathlib import PosixPath, Path

import nbformat as nbf

from ktx_parser.abs_format import AbsFormat
from ktx_parser.abs_getter import AbsGetter


class FormatJupyter(AbsFormat):
    def __init__(self, getter: AbsGetter):
        self.getter = getter

    def convert(self, destination_file: PosixPath):

        ktx_dict = self.getter.get_dict()
        destination_file = Path(destination_file)

        # Create cells sequence
        nb = nbf.v4.new_notebook()

        nb["cells"] = []

        # - Add header if any:
        if "header" in ktx_dict.keys():
            nb["cells"].append(nbf.v4.new_markdown_cell(ktx_dict["header"]))
        if "sub_header" in ktx_dict.keys():
            nb["cells"].append(nbf.v4.new_markdown_cell(ktx_dict["sub_header"]))
        if "jupyter_instruction" in ktx_dict.keys():
            nb["cells"].append(nbf.v4.new_markdown_cell(ktx_dict["jupyter_instruction"]))

        # - Add initializer
        nb["cells"].append(nbf.v4.new_code_cell(self.getter.get_initializer()))

        # - Get number of questions:
        num_questions = max([int(q.replace("q", "")) for q in ktx_dict.keys() if "q" in q])

        # - Add questions and empty spaces for answers
        for n in range(1, num_questions + 1):
            nb["cells"].append(nbf.v4.new_markdown_cell(f"#### {n}. " + ktx_dict[f"q{n}"]))
            nb["cells"].append(nbf.v4.new_code_cell(""))

        # Delete file if one with the same name is found
        if destination_file.exists():
            destination_file.unlink()

        # Write sequence to file
        nbf.write(nb, destination_file)

        print(f"\nFile {destination_file} created with {num_questions} questions.")
