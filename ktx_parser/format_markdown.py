from pathlib import PosixPath, Path
from typing import Optional

import mdutils

from ktx_parser.abs_format import AbsFormat
from ktx_parser.abs_getter import AbsGetter


class FormatMarkdown(AbsFormat):
    def __init__(self, getter: AbsGetter):
        self.getter = getter

    def convert(self, destination_file: PosixPath, subset_numbered_keys: Optional[str] = None):
        pass


# def create_markdown(qha_dict, destination_filename, with_hints=False, with_solutions=False):
#     # Create file name
#     if with_hints:
#         destination_filename += "_with_hints"
#     if with_solutions:
#         destination_filename += "_with_solutions"

#     # Initialise file
#     mdfile = mdutils.MdUtils(file_name=destination_filename)

#     # Add headers
#     mdfile.write(qha_dict["header"] + "\n")
#     mdfile.write(qha_dict["sub_header"] + "\n")

#     # - Get number of questions:
#     num_questions = max([int(q.replace("q", "")) for q in qha_dict.keys() if "q" in q])

#     # Add questions (and hint or answers if required)
#     for n in range(1, num_questions + 1):
#         mdfile.new_header(title=f"{n}. {qha_dict[f'q{n}']}", level=4)
#         if with_hints:
#             mdfile.write(f"`{qha_dict[f'h{n}']}`")
#         if with_solutions:
#             mdfile.insert_code(qha_dict[f"a{n}"], language="python")

#     # Delete file if one with the same name is found
#     if os.path.exists(destination_filename):
#         os.remove(destination_filename)

#     # Write sequence to file
#     mdfile.create_md_file()