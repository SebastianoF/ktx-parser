"""Decorations allow to customize prefixes and suffixes for each key and numbered key of a keyed text
before parsing it to a specified format.

Decorations (nothing to do with python decorators, only prefix and suffix for the rendered file)
are encoded in a dictionary as
```
{<prefix numbered key>: [<prefix value>, <key value>, <add key to prefix>]} 
```
How the converted file will look is responsibility of this python module and `format_<FORMAT>.py`.
"""

from typing import Tuple


DECORATIONS = {
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


def keys_to_decorations(getter_tag: str, format_tag: str, key: str) -> Tuple[str, str, bool]:
    """
    prefix, suffix, add_key_to_prefix = tags_to_deco(getter_tag, format_tag, key)
    if a value is found in the DECORATION dictionary. If keys are not found then
    it returns ('', '', False), so the decoration has no effect on the converted file.
    """
    if getter_tag not in DECORATIONS:
        return "", "", False
    if format_tag not in DECORATIONS[getter_tag]:
        return "", "", False
    if key not in DECORATIONS[getter_tag][format_tag]:
        return "", "", False
    return DECORATIONS[getter_tag][format_tag][key]
