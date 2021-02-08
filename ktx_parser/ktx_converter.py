from pathlib import PosixPath
from typing import Dict

from ktx_parser.abs_format import AbsFormat, ObjectView
from ktx_parser.abs_getter import AbsGetter

from format_jupyter import FormatJupyter
from format_markdown import FormatMarkdown


class KtxConverter:
    def __init__(self, path_to_source_folder: PosixPath, getter: AbsGetter):
        self.path_to_source_folder: PosixPath = path_to_source_folder
        self.getter: AbsGetter = getter

    def _get_nth_file(self, n: int):
        list_keyed_files = list(self.path_to_source_folder.glob("*.ktx"))
        try:
            return list_keyed_files[n]
        except IndexError as error:
            raise error(f"only {len(list_keyed_files)} found")

    def to_format(self) -> ObjectView[Dict[str, AbsFormat]]:
        dict_formats = {
            jupyter: FormatJupyter(self.getter).convert,
            markdown: FormatMarkdown(self.getter).convert,
        }
        return ObjectView(dict_formats)

    def get_dict(self, n: int) -> Dict:
        ktx_file = self._get_nth_file(n)
        return self.getter.get_dict(ktx_file)

    def get(self, n: int) -> AbsGetter:
        ktx_file = self._get_nth_file(n)
        return self.getter.get_entries(ktx_file)  # Dictionary with question, hint answer open to n
