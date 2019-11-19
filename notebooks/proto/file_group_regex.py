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

# %% {"pycharm": {"name": "#%%\n", "is_executing": false}, "jupyter": {"outputs_hidden": false}}
from typing import Dict, Pattern, Tuple

import re

from collections import defaultdict

from IPython.display import display

# %% {"jupyter": {"outputs_hidden": true}, "pycharm": {"is_executing": false}}
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


# %% {"pycharm": {"name": "#%%\n", "is_executing": false}, "jupyter": {"outputs_hidden": false}}
# Regular expression pattern for matching file names on disk.
FILE_GROUP_PATTERN = r"^(?P<basename>.*?)(?P<frames>\d+)?(?P<ext>\.\w*)*?$"
FILE_GROUP_RE = re.compile(FILE_GROUP_PATTERN)

# TODO: For now we do the work on the file name 
#  and not the full path to keep the complexity minimal...
def get_file_group_key(filename, disk_re: Pattern = None) -> Dict:
    """
    >>> get_file_group_key('file01_0040.rgb')
    {'basename': 'file01_', 'frames': '0040', 'ext': '.rgb'}
    >>> get_file_group_key('file.info.03.rgb.txt')
    {'basename': 'file.info.03', 'frames': 'None, 'ext': '.txt'}
    
    """
    check =  FILE_GROUP_RE.match or disk_re
    
    match = check(filename)
    groupdict = match.groupdict()
    
    return groupdict



# %% {"pycharm": {"name": "#%%\n", "is_executing": false}, "jupyter": {"outputs_hidden": false}}
# TODO: fix this edge case

get_file_group_key('file.info.03.txt')
# Should return...
# {'basename': 'file.info.03', 'frames': None, 'ext': '.txt'}

# %% {"pycharm": {"name": "#%%\n", "is_executing": false}, "jupyter": {"outputs_hidden": false}}
# display(files)
seqs = defaultdict(set)

for fp in files:
    groups = get_file_group_key(fp)
    key = '{basename}-{ext}'.format(**groups)
    seqs[key].add(groups['frames'])

display(seqs)
