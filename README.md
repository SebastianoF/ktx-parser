# ktx-parser

+ A keyed text is a text file divided into keys and values, made of text and parsed according to a configuration file.

+ The parser can contain html, markdown text, code, and general values with a custom format, and a custom way of distinguishing keys and text. 
The conversion can happen via a custom converter into a range of formats, such as markdown, jupyter notebook.


## Interface

```python
from ktx_parser import KtxGenerator

gen = KtxGenerator(<path to source folder>)

# file number to convert (in alphabetical order), if not given all files are converted.
n = 2
gen.to_format.jupyter(n)  
gen.to_format.markdown(n)
gen.to_all_formats(n)


# get individual parts:
file_n = gen.get_content(n)

# first question, hint and answer in the n-th file:
file_n["q1"] 
# or, if the key has no spaces,
file_n.q1 

# get the location of the source file
print(gen.source_file)
```


## Text example

```ktx
< A key

a value

< a key with no value

< q1
Question: how would you install this library?

< h1
Hint: well, with pip via the repo link.

< a1
# open a python terminal then:
pip install <repo url>
```


## Licence

This is an open source repository released under MIT license.
