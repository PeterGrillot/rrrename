# -*- coding: utf-8 -*-
from setuptools import setup

APP = ['main.py']
APP_NAME = "rrrename"
DATA_FILES = []

OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'static/rename.png',
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleGetInfoString': "rename",
        'CFBundleVersion': "0.1.0",
        'CFBundleShortVersionString': "0.1.0",
        'NSHumanReadableCopyright': u"Copyright © 2018, Peter Grillot, All Rights Reserved"
    }
}

setup(
    name=APP_NAME,
    app=APP,
    data_files=DATA_FILES,
)