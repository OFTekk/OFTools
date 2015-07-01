#
# coding:utf-8;

import ofspace


class WorldDataReader(object):
    def __init__(self, file):
        if not isinstance(file, str):
            raise TypeError
        self.file = file
