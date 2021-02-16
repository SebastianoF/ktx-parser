"""Decorators are prefix and suffix for each numbered key. 
They are encoded in a dictionary as
{<prefix numbered key>: [<prefix value>, <key value>, <add_key>]}, according
to the format of conversion."""

from typing import Tuple


DECORATORS = {
    "QuestionHintAnswer": {  # getter tag 1
        "jupyter": {  # format tag 1
            "header": ("# ", "", False),
            "sub_header": ("## ", "", False),
            "q": ("#### ", "\n\n", True),
        },
        "markdown": {  # format tag 2
            "header": ("# ", "\n\n", False),
            "sub_header": ("## ", "\n\n", False),
            "q": ("#### ", "\n\n", True),
            "h": ("`", "`\n\n", False),
            "a": ("```\n", "\n```\n\n", False),
        },
    }
}


def keys_to_decorators(getter_tag: str, format_tag: str, key: str) -> Tuple[str, str, bool]:
    """
    prefix, suffix = tags_to_deco(getter_tag, format_tag, key)
    if a value is found in the DECORATOR dictionary. If keys are not found then
    it returns ('', '', False)
    """
    if getter_tag not in DECORATORS:
        return "", "", False
    if format_tag not in DECORATORS[getter_tag]:
        return "", "", False
    if key not in DECORATORS[getter_tag][format_tag]:
        return "", "", False
    return DECORATORS[getter_tag][format_tag][key]
