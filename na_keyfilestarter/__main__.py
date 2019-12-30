#!/usr/bin/env python3

import argparse
import threading
import tempfile
from tkinter import *
from keyfilefs.fs import KeyfileFSOperations, mountKeyfileFS
from keyfilefs.gui import GUI, GUIPlugin


parser = argparse.ArgumentParser(description="""
    NeoAtlantis KeyfileFS Starter. Mounts a keyfile filesystem using FUSE
    under given mountpoint. 
""")

parser.add_argument("--config", "-c", required=True,
    help="""File containing configuration of this login. A such config file
        shall contain the URL to Volatile Password Generator. For details
        on formats of this file, read
        <https://github.com/neoatlantis/na_keyfilestarter>.
""")

parser.add_argument("--map", "-m", required=True, help="""
    The directory to be mapped into KeyfileFS. All filenames listed in this
    directory are salts, e.g. parameters used for calculating keyfile
    content. For each file in `MAP`, a corresponding keyfile matching
    that name will be created under `mountpoint`. The files in `mappoint`
    will be otherwise untouched.
""")

parser.add_argument("mountpoint", help="""
    Mount point for KeyfileFS. Must be an empty directory. This directory
    holds temporarily unlocked keyfiles that could be read by software, e.g.
    Keepass or Truecrypt/Veracrypt. Keyfiles are created by mapping each normal
    file given in `--map/-m` into a same-name file, whose content is calculated
    by deriving a secret from the common secret and that specific filename.
""")

args = parser.parse_args()



class NeoAtlantisKeyfileInput(GUIPlugin):

    def __init__(self, root):
        GUIPlugin.__init__(self, root)
        self.secretCallback = None
        self.__initWidgets()

    def __initWidgets(self):
        pass

    def onSecretGenerated(self, callback):
        self.secretCallback = callback


keyfileFS = KeyfileFSOperations()



fst = threading.Thread(
    target=mountKeyfileFS,
    args=(keyfileFS, args.mountpoint)
)
fst.start()



gui = GUI(mountpoint=args.mountpoint, fs=keyfileFS, plugin=NeoAtlantisKeyfileInput)

