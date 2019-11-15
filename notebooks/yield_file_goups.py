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

# %% {"jupyter": {"outputs_hidden": true}}
from typing import Dict, Pattern, Tuple

from dataclasses import dataclass

from IPython.display import display


# %% {"pycharm": {"name": "#%%\n"}, "jupyter": {"outputs_hidden": false}}
@dataclass
class FileData:
    
    dir: str
    basename: str
    extension: str


# %% {"pycharm": {"name": "#%%\n"}, "jupyter": {"outputs_hidden": false}}

def yield_file_groups(file_seq_map):
    
    for (dirname, basename, ext), file_paths in file_seq_map.items():
        
        fd = FileData(dirname, basename, ext)
        
        if file_paths > 1:
            yield Fileobj(file_data=fd)
        else:
            yield FileSequence(file_data=fd, file_paths=file_paths)
            


# %% {"pycharm": {"name": "#%%\n"}, "jupyter": {"outputs_hidden": false}}
    file_seq_map = {
        
    }

# %% {"pycharm": {"name": "#%%\n"}, "jupyter": {"outputs_hidden": false}}
    file_groups = yield_file_groups(file_seq_map)
    file_groups

