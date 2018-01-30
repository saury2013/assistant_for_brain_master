# -*- coding: utf-8 -*-
__author__ = 'Allen'

from flask import request,Flask
import os,time,threading

app = Flask(__name__)

setting = {
    "start":{
        "dX":358,
        "dY":900 #1200
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

def run_adb(option):
    time.sleep(4)
    os.popen("adb shell input tap {0} {1}".format(setting[option]["dX"], setting[option]["dY"]))
    if option == "continue":
        time.sleep(5)
        os.popen("adb shell input tap {0} {1}".format(setting["start"]["dX"], setting["start"]["dY"]))


@app.route('/',methods=['GET'])
def operate_phone():
    option = request.args.get("option")
    print(option)
    #开启一个线程去操作手机
    t = threading.Thread(target=run_adb,args=(option,))
    t.start()
    return option

app.run(host='localhost',port=5050)