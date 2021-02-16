from pathlib import PosixPath, Path
from typing import Optional

import mdutils

from ktx_parser.abs_format import AbsFormat
from ktx_parser.abs_getter import AbsGetter


class FormatMarkdown(AbsFormat):
    def __init__(self, getter: AbsGetter):
        self.getter = getter
        self.decorator = DECORATORS.get(self.getter.get_getter_tag())

    @staticmethod
    def get_format_tag() -> str:
        return "markdown"

    def convert(self, destination_file: PosixPath, subset_numbered_keys: Optional[str] = None):

        ktx_dict = self.getter.get_dict()
        destination_file = Path(destination_file)

        # - Initialise file
        md_file = mdutils.MdUtils(file_name=str(destination_file))

        # - load decorators
        if self.decorator is not None:
            self.decorator = self.decorator.get(self.get_format_tag())

        # - Write header if any:
        for hdr_keys in self.getter.get_headers_keys():
            if self.decorator is not None:
                deco = self.decorator.get(hdr_keys)
                prefix = deco[0] if deco is not None else ""
                suffix = deco[1] if deco is not None else ""
            else:
                prefix = ""
                suffix = ""
            # TODO call a function key to decorator returning ['', ''] if no keys for two layers, otherwise
            # returning the corresponding key in the input decorator dictionary.
            # prefix, suffix = tags_to_deco(getter_tag, format_tag, key), under decorators.py
            # use it below as well.

            md_file.write(prefix + ktx_dict[hdr_keys] + suffix)

        # - Write numbered keys if any:
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
                    md_file.write(ktx_dict[k])

        # Delete file if one with the same name is found
        if destination_file.exists():
            destination_file.unlink()

        # Write sequence to file
        md_file.create_md_file()

        print(f"\nFile {destination_file} created with {num_numbered_keys_found} numbered keys.")


#     # Add questions (and hint or answers if required)
#     for n in range(1, num_questions + 1):
#         mdfile.new_header(title=f"{n}. {qha_dict[f'q{n}']}", level=4)
#         if with_hints:
#             mdfile.write(f"`{qha_dict[f'h{n}']}`")
#         if with_solutions:
#             mdfile.insert_code(qha_dict[f"a{n}"], language="python")
