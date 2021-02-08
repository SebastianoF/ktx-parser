# Here is where the whole file generation is happening. Only module external to the ktx_reader.

import os
import glob
import shutil


import pathlib


from .ktx_reader import getter

GENERATORS = pathlib.Path(__file__).parent.absolute()
ROOT = GENERATORS.parent


def initialize_getter(part_num: int):

    root = pathlib.Path(ROOT)

    return getter.KtxGetter(part_num, root)


# TODO: refactor the part below using the new classes instead of the spaghetti code.
# then delete generate and initialize.

# then turn ktx parser into a pip installable library, with a complete bumpversion instance for releases
if __name__ == "__main__":

    from generate import ktx_to_dict, create_markdown, create_jupyter_notebook

    HERE = os.path.dirname(os.path.realpath(__file__))

    jupyter_destination_folder = os.path.join(HERE, "notebooks")
    markdown_destination_folder = os.path.join(HERE, "markdown_notes")

    for p in range(1, 7):
        ktx_file = os.path.join(HERE, "source", f"part{p}.ktx")
        assert os.path.exists(ktx_file), f"source file {ktx_file} does not exist"

        qha_dict = ktx_to_dict(ktx_file)

        part_name = f"part{p}"

        create_jupyter_notebook(
            qha_dict=qha_dict,
            destination_filename=os.path.join(jupyter_destination_folder, part_name + ".ipynb"),
            part_num=p,
        )

        for h, s in [(False, False), (False, True), (True, False), (True, True)]:
            create_markdown(qha_dict=qha_dict, destination_filename=part_name, with_hints=h, with_solutions=s)

    # As can not create markdown files at a specified folder (!!), move all the md files from root
    # to specified folder after creation
    md_files_in_root = glob.glob(os.path.join(HERE, "part*.md"))

    md_files_in_destination = [os.path.join(markdown_destination_folder, os.path.basename(f)) for f in md_files_in_root]
    for md_old, md_new in zip(md_files_in_root, md_files_in_destination):
        shutil.move(md_old, md_new)
