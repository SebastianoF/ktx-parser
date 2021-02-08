"""
Part of the code is from numpy-100, under MIT licence
https://github.com/rougier/numpy-100/blob/master/LICENSE.txt
"""
import os
import glob
import shutil

import nbformat as nbf
import mdutils


HERE = os.path.dirname(os.path.realpath(__file__))


def ktx_to_dict(input_file, keystarter="<"):
    """ parsing keyed text to a python dictionary. """
    answer = dict()

    with open(input_file, "r+", encoding="utf-8") as f:
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


def dict_to_ktx(input_dict, output_file, keystarter="<"):
    """ Store a python dictionary to a keyed text"""
    with open(output_file, "w+") as f:
        for k, val in input_dict.items():
            f.write(f"{keystarter} {k}\n")
            f.write(f"{val}\n\n")


def create_jupyter_notebook(qha_dict, destination_filename, part_num=0):
    """ Programmatically create jupyter notebook """

    # Create cells sequence
    nb = nbf.v4.new_notebook()

    nb["cells"] = []

    # - Add header:
    nb["cells"].append(nbf.v4.new_markdown_cell(qha_dict["header"]))
    nb["cells"].append(nbf.v4.new_markdown_cell(qha_dict["sub_header"]))
    nb["cells"].append(nbf.v4.new_markdown_cell(qha_dict["jupyter_instruction"]))

    # - Add initialisation
    nb["cells"].append(nbf.v4.new_code_cell("%run ../initialize.py " + str(part_num)))

    # - Get number of questions:
    num_questions = max([int(q.replace("q", "")) for q in qha_dict.keys() if "q" in q])

    # - Add questions and empty spaces for answers
    for n in range(1, num_questions + 1):
        nb["cells"].append(nbf.v4.new_markdown_cell(f"#### {n}. " + qha_dict[f"q{n}"]))
        nb["cells"].append(nbf.v4.new_code_cell(""))

    # Delete file if one with the same name is found
    if os.path.exists(destination_filename):
        os.remove(destination_filename)

    # Write sequence to file
    nbf.write(nb, destination_filename)

    print()
    print(f"File {destination_filename} created with {num_questions} questions.")


def create_markdown(qha_dict, destination_filename, with_hints=False, with_solutions=False):
    # Create file name
    if with_hints:
        destination_filename += "_with_hints"
    if with_solutions:
        destination_filename += "_with_solutions"

    # Initialise file
    mdfile = mdutils.MdUtils(file_name=destination_filename)

    # Add headers
    mdfile.write(qha_dict["header"] + "\n")
    mdfile.write(qha_dict["sub_header"] + "\n")

    # - Get number of questions:
    num_questions = max([int(q.replace("q", "")) for q in qha_dict.keys() if "q" in q])

    # Add questions (and hint or answers if required)
    for n in range(1, num_questions + 1):
        mdfile.new_header(title=f"{n}. {qha_dict[f'q{n}']}", level=4)
        if with_hints:
            mdfile.write(f"`{qha_dict[f'h{n}']}`")
        if with_solutions:
            mdfile.insert_code(qha_dict[f"a{n}"], language="python")

    # Delete file if one with the same name is found
    if os.path.exists(destination_filename):
        os.remove(destination_filename)

    # Write sequence to file
    mdfile.create_md_file()


if __name__ == "__main__":

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
