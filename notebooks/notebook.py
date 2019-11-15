# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + {"pycharm": {"is_executing": false}}
import os, pathlib

import fileseq

# + {"pycharm": {"is_executing": false}}
cwd =  pathlib.Path(os.getcwd()).parent
path = cwd.joinpath('tests/broken_seq')
seqs = fileseq.findSequencesOnDisk(path.as_posix())
seqs

# + {"pycharm": {"is_executing": false}}
s = seqs[2]
# dir(s)

# + {"pycharm": {"is_executing": false}}
s.padding()

# + {"pycharm": {"is_executing": false}}
path.as_posix()

# + {"pycharm": {"is_executing": false}}
cwd =  pathlib.PurePath(os.getcwd()).parent
path = cwd.joinpath('tests/broken_seq')
# dir(path)

# + {"pycharm": {"name": "#%%\n", "is_executing": false}}
PAD_MAP = {"#": 4, "@": 1}

# Regular expression for matching a file sequence string.
# Example: /film/shot/renders/bilbo_bty.1-100#.exr
# Example: /film/shot/renders/bilbo_bty.1-100@.exr
# Example: /film/shot/renders/bilbo_bty.1-100@@@@#.exr
# Example: /film/shot/renders/bilbo_bty.1-100%04d.exr
SPLIT_PATTERN = r"((?:[-\d][-:,xy\d]*)?)([{0}]+|%(?:\d)*d|\$F(?:\d)*)".format(''.join(PAD_MAP))
print(SPLIT_PATTERN)
