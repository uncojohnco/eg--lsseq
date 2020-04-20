#!/usr/bin/env python3

import logging

import lss.dataclass.base
import lss.dataclass.item
import lss.dataclass.sequence

# https://realpython.com/python-logging-source-code/#library-vs-application-logging-what-is-nullhandler
logging.getLogger(__name__).addHandler(logging.NullHandler())


SubstrPos = lss.dataclass.base.SubstrPos
SubstrMatch = lss.dataclass.base.SubstrMatch

Item = lss.dataclass.item.Item
FileItem = lss.dataclass.item.FileItem
FileSequence = lss.dataclass.sequence.FileSequence
SequenceStrParts = lss.dataclass.sequence.SequenceStrParts
