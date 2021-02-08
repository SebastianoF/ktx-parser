from typing import Dict
from abs_getter import AbsGetter


class GetterQuestionHintAnswer(AbsGetter):
    def __init__(self, input_file):
        pass

    def _ktx_to_dict(keystarter="<") -> Dict:
        """ parsing keyed text to a python dictionary. """
        answer = dict()

        with open(self.input_file, "r+", encoding="utf-8") as f:
            lines = f.readlines()

        k, val = "", ""
        for line in lines:
            if line.startswith(keystarter):
                k = line.replace(keystarter, "").strip()
                val = ""
            else:
                val += line

            if k:
                answer.update({k: val.strip()})

        return answer