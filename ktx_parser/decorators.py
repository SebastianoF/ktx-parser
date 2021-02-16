"""Decorators are prefix and suffix for each numbered key. 
They are encoded in a dictionary as
{<prefix numbered key>: [<prefix value>, <key value>]}, according
to the format of conversion."""


decorators = {
    "QuestionHintAnswer": {
        "jupyter": {
            "header": ["", ""],
            "sub_header": ["", ""],
            "q": ["#### ", "\n\n"],
        },
        "markdown": {
            "header": ["", ""],
            "q": ["#### ", "\n\n"],
            "h": ["`", "`\n"],
            "a": ["```", "```\n"],
        },
    }
}
