"""Decorators are prefix and suffix for each numbered key. 
They are encoded in a dictionary as
{<prefix numbered key>: [<prefix value>, <key value>]}, according
to the format of conversion."""

from typing import Tuple


DECORATORS = {
    "QuestionHintAnswer": {  # getter tag 1
        "jupyter": {  # format tag 1
            "header": ["# ", ""],
            "sub_header": ["## ", ""],
            "q": ["#### ", "\n\n"],
        },
        "markdown": {  # format tag 2
            "header": ["# ", "\n\n"],
            "sub_header": ["## ", "\n\n"],
            "q": ["#### ", "\n\n"],
            "h": ["`", "`\n\n"],
            "a": ["```\n", "\n```\n\n"],
        },
    }
}


def keys_to_decorators(getter_tag: str, format_tag: str, key: str) -> Tuple[str, str]:
    """
    prefix, suffix = tags_to_deco(getter_tag, format_tag, key)
    if a value is found in the DECORATOR dictionary. If keys are not found then
    it returns ('', '')
    """
    if getter_tag not in DECORATORS:
        return "", ""
    if format_tag not in DECORATORS[getter_tag]:
        return "", ""
    if key not in DECORATORS[getter_tag][format_tag]:
        return "", ""
    return DECORATORS[getter_tag][format_tag][key]
