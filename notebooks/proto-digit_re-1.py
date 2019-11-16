# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% {"pycharm": {"is_executing": false}, "jupyter": {"outputs_hidden": true}}
import os
import re

from IPython.display import display

# %% {"pycharm": {"name": "#%%\n", "is_executing": false}, "jupyter": {"outputs_hidden": false}}
files_pre = """
alpha.txt
file01_0040.rgb
file01_0041.rgb
file01_0042.rgb
file01_0043.rgb
file02_0044.rgb
file02_0045.rgb
file02_0046.rgb
file02_0047.rgb
file1.03.rgb
file2.03.rgb
file3.03.rgb
file4.03.rgb
file.info.03.rgb
"""

files = files_pre.split()
display(files)

# %% {"pycharm": {"name": "#%%      \n", "is_executing": false}, "jupyter": {"outputs_hidden": false}}
digits_re = re.compile(r'\d+')

item = files[1]


_path = os.path.abspath(str(item))

dirname, filename = os.path.split(_path)

name = filename

digits = digits_re.findall(name)
parts = digits_re.split(name)


# %% {"pycharm": {"name": "#%%      \n", "is_executing": false}, "jupyter": {"outputs_hidden": false}}

f1_name = 'file01_0040.rgb'
f2_name = 'file01_0041.rgb'


l1 = [m for m in digits_re.finditer(f1_name)]
l2 = [m for m in digits_re.finditer(f2_name)]

