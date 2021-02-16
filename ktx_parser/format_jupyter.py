from pathlib import PosixPath, Path
from typing import Optional

import nbformat as nbf

from ktx_parser.abs_format import AbsFormat
from ktx_parser.abs_getter import AbsGetter
from ktx_parser.decorators import keys_to_decorators


class FormatJupyter(AbsFormat):
    def __init__(self, getter: AbsGetter):
        self.getter = getter

    @staticmethod
    def get_format_tag() -> str:
        return "jupyter"

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

        # - Write numbered keys if any:
        n_keys = self.getter.get_quantity_numbered_keys()
        numbered_keys = self.getter.get_numbered_keys()

        if isinstance(numbered_keys, dict):
            if subset_numbered_keys is None:
                raise ValueError("Please specify a key for the provided dictionary of keyed text")
            numbered_keys = numbered_keys[subset_numbered_keys]

        num_numbered_keys_found = 0
        for key in numbered_keys:
            for n in range(n_keys[0], n_keys[1] + 1):
                k = f"{key}{n}"
                if k in ktx_dict.keys():
                    num_numbered_keys_found += 1
                    nb["cells"].append(nbf.v4.new_markdown_cell(f"#### {n}. " + ktx_dict[k]))
                    nb["cells"].append(nbf.v4.new_code_cell(""))

        # - Delete file if one with the same name is found
        if destination_file.exists():
            destination_file.unlink()

        # - Save result to file
        nbf.write(nb, str(destination_file))
        print(f"File {destination_file} created with {num_numbered_keys_found} numbered keys.")
