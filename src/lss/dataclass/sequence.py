


class FileSequence:

    _item: FileItem
    _items: List[FileItem]

    def __init__(self, fileitem: FileItem):

        super(FileSequence, self).__init__(fileitem)

        self._dirname = self._item.dirname
