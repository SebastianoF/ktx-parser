#!/usr/bin/python
"""
Part of the code is from numpy-100, under MIT licence
https://github.com/rougier/numpy-100/blob/master/LICENSE.txt
"""

import sys
import os


from generate import ktx_to_dict


if __name__ == "__main__":

    here = os.path.dirname(os.path.realpath(__file__))

    ktx_file = os.path.join(here, "source", f"part{sys.argv[1]}.ktx")

    qha_dict = ktx_to_dict(ktx_file)

    def question(n):
        print(f"{n}. " + qha_dict[f"q{n}"])

    def hint(n):
        print(qha_dict[f"h{n}"])

    def answer(n):
        print(qha_dict[f"a{n}"])
