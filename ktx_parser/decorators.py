"""Decorators are prefix and suffix for each numbered key. 
They are encoded in a dictionary as
{<prefix numbered key>: [<prefix value>, <key value>]}, according
to the format of conversion."""


DECORATORS = {
    "QuestionHintAnswer": {  # ktx tag 1
        "jupyter": {  # format tag 1
            "header": ["", ""],
            "sub_header": ["", ""],
            "q": ["#### ", "\n\n"],
        },
        "markdown": {  # format tag 2
            "header": ["", ""],
            "q": ["#### ", "\n\n"],
            "h": ["`", "`\n"],
            "a": ["```", "```\n"],
        },
    }
}
