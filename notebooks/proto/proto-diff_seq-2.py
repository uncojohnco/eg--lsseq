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

# %% {"pycharm": {"name": "#%%\n"}, "jupyter": {"outputs_hidden": false}}
import os
import re

import logging
from typing import List, Match, Union

from IPython.display import display

log = logging.getLogger('scratch-2')
log.setLevel(logging.DEBUG)

DIGITS_RE = re.compile(r'\d+')

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

file01.0000.v03.rgb
file02.0000.v03.rgb
file03.0000.v03.rgb
"""

files = files_pre.split()
display(files)


# %% {"pycharm": {"name": "#%%\n", "is_executing": false}, "jupyter": {"outputs_hidden": false}}
class Item:

    def __init__(self, item):

        self._item = item
        self._path = os.path.abspath(str(item))

        self._dirname, self._filename = os.path.split(self._path)

        self._digits = DIGITS_RE.findall(self.name)
        self._parts = DIGITS_RE.split(self.name)

    def is_sibling(self, item: Union[str, 'Item']) -> bool:

        if not isinstance(item, Item):
            item = Item(item)

        if self._parts != item._parts:
            return False

        diff_result = diff_sequence(self.name, item.name)
        is_sibling = len(diff_result) == 1

        return is_sibling

    @property
    def name(self) -> str:
        return self._filename

    @property
    def parts(self) -> List[str]:
        return self._parts
    
    @property
    def digits(self) -> List[int]:
        return self._digits

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        n = self.name
        return '<lss.Item "{n}">'
    

def diff_sequence(name1: str, name2: str, strict=True) -> List:
    
    def _same_seq(match1: Match, match2: Match) -> bool:
        
        start1, start2 = match1.start(), match2.start()
        group1, group2 = match1.group(), match2.group()

        if start1 != start2:
            return False
    
        if group1 == group2:
            return False
    
        if strict is True and len(group1) != len(group2):
            return False

        return True
    
    log.debug(f'diff: "{name1} {name2}')

    matches1 = [m for m in DIGITS_RE.finditer(name1)]
    matches2 = [m for m in DIGITS_RE.finditer(name2)]

    if not len(matches1) == len(matches2):
        return []

    diff_result = []

    for m1, m2 in zip(matches1, matches2):
        
        if not _same_seq(m1, m2):
            continue

        data = {
            'start': m1.start(),
            'end': m1.end(),
            'frames': (m1.group(), m2.group())
        }
        diff_result.append(data)

    return diff_result
        


# %% {"pycharm": {"name": "#%%\n", "is_executing": false}, "jupyter": {"outputs_hidden": false}}
items = list(map(Item, files))
    
for ii in items:
    print(f'{ii} - {ii.parts}, {ii.digits}')

# %% {"pycharm": {"name": "#%%\n", "is_executing": false}, "jupyter": {"outputs_hidden": false}}
f1_name = 'file01_0040.rgb'
f2_name = 'file01_0041.rgb'


i1 = Item(f1_name)

s = i1.is_sibling(f2_name)
