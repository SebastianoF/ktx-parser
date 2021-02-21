# ktx-parser

+ A keyed text is a text file divided into keys and values, made of text and parsed according to a configuration file.

+ The parser can contain html, markdown text, code, and general values with a custom format, and a custom way of distinguishing keys and text. 
The conversion can happen via a custom converter into a range of formats. At the moment implemented for markdown, and jupyter notebook, but extensible to other formats.


## Interface



## Where to start

Install the library in a virtualenvironment with pip, then run the example in the examples folder:
```
virtualenv venv -p python3.8 
source venv/bin/activate
pip install -r requirements.txt

python examples/convert_examples.py 
```
## Licence

This is an open source repository released under MIT license.
