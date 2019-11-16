#!/usr/bin/env python3

import pathlib

import lss.render
import lss.filecomposer
import lss.fileseqformatter

FileComposer = lss.filecomposer.FileComposer
FileSeqFormatter = lss.fileseqformatter.FileSeqFormatter


def run(dir_path: str) -> str:

    path = pathlib.Path(dir_path)

    children = path.iterdir()

    file_composer = FileComposer(children)
    file_groups = file_composer.do_it()

    formatter = FileSeqFormatter(file_groups)

    result = formatter.do_it()

    # Render to Shell
    output = '\n'.join(result)

    return output
