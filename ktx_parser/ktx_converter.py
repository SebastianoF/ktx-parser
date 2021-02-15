from pathlib import PosixPath
from typing import Dict

from ktx_parser.object_view import ObjectView
from ktx_parser.abs_getter import AbsGetter

from ktx_parser.format_jupyter import FormatJupyter
from ktx_parser.format_markdown import FormatMarkdown


class KtxConverter:
    def __init__(self, path_to_source_file: PosixPath, getter: AbsGetter):
        self.path_to_source_file: PosixPath = path_to_source_file
        self.getter: AbsGetter = getter

    def to_format(self) -> ObjectView:
        dict_formats = {
            "jupyter": FormatJupyter(self.getter).convert,
            "markdown": FormatMarkdown(self.getter).convert,
            # add here other formats!
        }
        return ObjectView(dict_formats)

    def get_dict(self) -> Dict:
        if not self.path_to_source_file.suffix == ".ktx":
            raise ValueError("Input source file is not a keyed text file.")
        return self.getter.get_dict(self.path_to_source_file)

    def get(self) -> AbsGetter:
        return self.getter.get_entries(self.path_to_source_file)  # Dictionary with question, hint answer open to n
