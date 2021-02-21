"""
Example of converting the files in the `source` folder.
"""
from pathlib import Path


from ktx_parser import KtxConverter, GetterQuestionHintAnswer


HERE = Path(__file__).parent

# Input folder
SOURCE = HERE / "source"

# Output folder
CNV_JUPYTER = HERE / "converted_to_jupyter"
CNV_MARKDOWN = HERE / "converted_to_markdown"


if __name__ == "__main__":

    CNV_JUPYTER.mkdir(exist_ok=True)
    CNV_MARKDOWN.mkdir(exist_ok=True)

    for p in SOURCE.glob("*ktx"):
        getter = GetterQuestionHintAnswer(input_file=p)
        converter = KtxConverter(getter=getter)

        converter.to_format().jupyter(  # pylint: disable=no-member
            str(CNV_JUPYTER / Path(p.name).stem) + ".ipynb",
            subset_numbered_keys="question",
        )

        converter.to_format().markdown(  # pylint: disable=no-member
            str(CNV_MARKDOWN / Path(p.name).stem) + "_questions",
            subset_numbered_keys="question",
        )

        converter.to_format().markdown(  # pylint: disable=no-member
            str(CNV_MARKDOWN / Path(p.name).stem) + "_questions_and_hints.md",
            subset_numbered_keys="question_hint",
        )

        converter.to_format().markdown(  # pylint: disable=no-member
            str(CNV_MARKDOWN / Path(p.name).stem) + "_questions_and_answers.md",
            subset_numbered_keys="question_answer",
        )