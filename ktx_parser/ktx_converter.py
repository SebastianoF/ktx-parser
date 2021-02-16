from pathlib import PosixPath
from typing import Dict

from ktx_parser.object_view import ObjectView
from ktx_parser.abs_getter import AbsGetter

from ktx_parser.format_jupyter import FormatJupyter
from ktx_parser.format_markdown import FormatMarkdown


class KtxConverter:
    def __init__(self, getter: AbsGetter):
        self.getter: AbsGetter = getter
        self.input_file: PosixPath = self.getter.input_file

    def to_format(self) -> ObjectView:
        dict_formats = {
            "jupyter": FormatJupyter(self.getter).convert,
            "markdown": FormatMarkdown(self.getter).convert,
            # add here other formats!
        }
        return ObjectView(dict_formats)

    def get_dict(self) -> Dict:
        if not self.input_file.suffix == ".ktx":
            raise ValueError("Input source file is not a keyed text file.")
        return self.getter.get_dict(self.input_file)

    def get(self) -> AbsGetter:
        return self.getter.get_entries(self.input_file)
