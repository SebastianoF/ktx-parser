from typing import Dict, List, Union
from pathlib import PosixPath, Path
import random

from ktx_parser.abs_getter import AbsGetter
from ktx_parser.object_view import ObjectView


class GetterQuestionHintAnswer(AbsGetter):
    def __init__(self, input_file: PosixPath):
        self.input_file: PosixPath = input_file
        self.keystarter: str = "<"
        self.ktx_dict: Dict = None
        self._num_keys: List = None
        self._ktx_to_dict()

    def _ktx_to_dict(self) -> Dict:
        """ parsing keyed text to a python dictionary. """
        self.input_file = Path(self.input_file)
        if not self.input_file.exists():
            raise ValueError(f"Input path {self.input_file} does not exist.")

        with open(self.input_file, "r+", encoding="utf-8") as f:
            lines = f.readlines()

        ktx_dict = dict()
        k, val = "", ""
        for line in lines:
            if line.startswith(self.keystarter):
                k = line.replace(self.keystarter, "").strip()
                val = ""
            else:
                val += line

            if k:
                ktx_dict.update({k: val.strip()})

        self.ktx_dict = ktx_dict
        self._num_keys = [int(q.replace("q", "")) for q in self.ktx_dict if "q" in q]

    def _dict_to_ktx(self, output_file: PosixPath):
        """ Store a python dictionary to a keyed text"""
        with open(output_file, "w+") as f:
            for k, val in self.ktx_dict.items():
                f.write(f"{self.keystarter} {k}")
                f.write(f"{val}")

    @staticmethod
    def get_getter_tag() -> str:
        return "QuestionHintAnswer"

    @staticmethod
    def get_headers_keys() -> Union[List, Dict]:
        return ["header", "sub_header"]

    @staticmethod
    def get_numbered_keys() -> Union[List, Dict]:
        return {
            "question": ["q"],
            "question_hint": ["q", "h"],
            "question_answer": ["q", "a"],
            "question_hint_answer": ["q", "h", "a"],
        }

    def get_interactive_initializer(self):
        if "interactive_initialisation" in self.ktx_dict.keys():
            return self.ktx_dict.get("interactive_initialisation")
        return None

    def get_dict(self):
        return self.ktx_dict

    def get_quantity_numbered_keys(self) -> (int, int):
        return min(self._num_keys), max(self._num_keys)

    def get_entries(self):
        """Returns the object view of what the user will query"""

        def warn(n):
            if n not in self._num_keys:
                print(f"No keys for {n}. Keys specified are in {self._num_keys}")

        def question(num: int):
            warn(num)
            print(self.ktx_dict.get(f"q{num}"))

        def hint(num: int):
            warn(num)
            print(self.ktx_dict.get(f"h{num}"))

        def answer(num: int):
            warn(num)
            print(self.ktx_dict.get(f"a{num}"))

        def random_question():
            num = random.sample(self._num_keys, 1)[0]
            print(f"{num}. " + self.ktx_dict.get(f"q{num}"))

        dict_qha = dict(
            question=question,
            hint=hint,
            answer=answer,
            random_question=random_question,
        )

        return ObjectView(dict_qha)
