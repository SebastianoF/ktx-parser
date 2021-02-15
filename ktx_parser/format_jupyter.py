from pathlib import PosixPath, Path
from typing import Optional

import nbformat as nbf

from ktx_parser.abs_format import AbsFormat
from ktx_parser.abs_getter import AbsGetter


class FormatJupyter(AbsFormat):
    def __init__(self, getter: AbsGetter):
        self.getter = getter

    def convert(self, destination_file: PosixPath, subset_numbered_keys: Optional[str] = None):

        ktx_dict = self.getter.get_dict()
        destination_file = Path(destination_file)

        # Create cells sequence
        nb = nbf.v4.new_notebook()

        nb["cells"] = []

        # - Add header if any:
        for hdr_keys in self.getter.get_headers_keys():
            nb["cells"].append(nbf.v4.new_markdown_cell(ktx_dict[hdr_keys]))

        # - Add initializer - for interactive formats
        nb["cells"].append(nbf.v4.new_code_cell(self.getter.get_initializer()))

        # - Get numbered keys:
        n_keys = self.getter.get_quantity_numbered_keys()
        numbered_keys = self.getter.get_numbered_keys()

        if isinstance(numbered_keys, dict):
            numbered_keys = numbered_keys[subset_numbered_keys]

        num_numbered_keys_found = 0
        for key in numbered_keys:
            # - Add questions and empty spaces for answers
            for n in range(n_keys[0], n_keys[1] + 1):
                k = f"{key}{n}"
                if k in ktx_dict.keys():
                    num_numbered_keys_found += 1
                    nb["cells"].append(nbf.v4.new_markdown_cell(f"#### {n}. " + ktx_dict[k]))
                    nb["cells"].append(nbf.v4.new_code_cell(""))

        # Delete file if one with the same name is found
        if destination_file.exists():
            destination_file.unlink()

        # Write sequence to file
        nbf.write(nb, destination_file)

        print(f"\nFile {destination_file} created with {num_numbered_keys_found} numbered keys.")
