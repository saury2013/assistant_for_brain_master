# -*- coding: utf-8 -*-
__author__ = 'Allen'

import os

setting = {
    "start":{
        "dX":358,
        "dY":1200
    },
    "continue":{
        "dX":358,
        "dY":944
    },
    "option0":{
        "dX":324,
        "dY":721
    },
    "option1":{
        "dX":324,
        "dY":841
    },
    "option2":{
        "dX":324,
        "dY":963
    },
    "option3":{
        "dX":324,
        "dY":1090
    },
}

def auto_click(position):
    _shell = "adb shell input tap {0} {1}"
    os.popen(_shell.format(setting[position]['dX'],setting[position]['dX']))