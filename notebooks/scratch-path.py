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

# %% {"pycharm": {"is_executing": false}}
import os
import pathlib
import fileseq

# %%
p = 
path = pathlib.Path("/here/your/path/file.txt")
print(path.parent)

# %% {"jupyter": {"outputs_hidden": false}, "pycharm": {"name": "#%%\n"}}

path, frames, self._pad, self._ext = SPLIT_RE.split(sequence, 1)
self._dir, self._base = os.path.split(path)

# %%
ff = """
file1.03.rgb
file2.03.rgb
file3.03.rgb
file4.03.rgb
""".split()
# print(f)

files = list(map(pathlib.Path, ff))
# files

f = files[0]

# %%
f.name

# %%
dir(f)

# %%

# %% {"pycharm": {"name": "#%%\n", "is_executing": false}, "jupyter": {"outputs_hidden": false}}
cwd =  pathlib.Path(os.getcwd()).parent
path = cwd.joinpath('tests/broken_seq')
seqs = fileseq.findSequencesOnDisk(path.as_posix())
seqs

# %% {"pycharm": {"name": "#%%\n", "is_executing": false}, "jupyter": {"outputs_hidden": false}}
p = os.path.abspath('.')
print(p)
