#!/usr/bin/env python3

import os
import yaml

class Config:

    def __init__(self, readfrom):
        self.__doc = yaml.load(open(readfrom, "r").read())

        self.basedir = os.path.dirname(os.path.realpath(readfrom))
