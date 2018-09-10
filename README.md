# handybelt
A collection of python functions that I've found useful over the years.

I'm using the following tutorial to upload my project to git so that it can be installed via pip:
https://packaging.python.org/tutorials/packaging-projects/#create-an-account

<!--
  1) Create project from git because it automatically creates:
       - README.md
       - LICENSE
  2) Create a __init__.py file inside project/project directory
  3) Create a setup.py file in project directory (copy from above website)

 -->

<!-- Install/upgrade setuptools/wheel (not every time)-->
<!-- python -m pip install --user --upgrade setuptools wheel -->

<!-- Install/update twine (not every time) -->
<!-- python3 -m pip install --user --upgrade twine -->

<!-- Generate distribution: -->
python setup.py sdist bdist_wheel

<!-- Upload distribution: -->
twine upload dist/*

<!-- Test newly uploaded distribution: -->
python -m pip install handybelt

<!-- Test project: -->
python
import project


## Features
  ✔ screenshot - Takes a screenshot and saves it to a file

  ✔ transparentizeBG - Makes the background of an image transparent

  ✔ crop - Auto-crop an image

  ✔ buildlatex - Builds a latex file to generate a pdf (and deletes temp files)

  ✔ cleartempfiles - Deletes temporary files made from latex build

  ✔ resize - Resizes an image file

  ✔ pdf2img - Generates image file from a PDF file

## New features to add:
  ☐ squarify - Makes an image square in shape by cropping then padding

  ☐ grayscale - Makes an image gray-scale

  ☐ newlatex - creates a new latex folder and file with typical packages

  ☐ newlatexPPT - creates a new latex PPT folder and file with typical packages

  ☐ pyfind - prints a list of files in all subdirectories (with given extension) that contains a given keyword


## Example use:

python -m screenshot

To see options, use

python -m screenshot --help



