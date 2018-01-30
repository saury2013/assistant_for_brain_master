# -*- coding: utf-8 -*-
__author__ = 'Allen'

from urllib.parse import quote
import string
import requests


request_json = {
	"data": {
		"quiz": "豫是哪个省份的简称？",
		"options": ["山西", "陕西", "河北", "河南"],
		"num": 4,
		"school": "理科",
		"type": "地理",
		"typeID": 9,
		"contributor": "🎶Cuckoo Z。",
		"partner": 0,
		"endTime": 1517125055,
		"curTime": 1517125040,
		"myBuff": {}
	},
	"errcode": 0
}

# question = request_json['data']['quiz']
# options = request_json['data']['options']
#
#
# answer_option = request_json['data']['num']
# answer = options[int(answer_option)-1]
# print(answer)
#
# def cat_test(path):
#     _question = ''
#     _options = []
#     if path == 1:
#         question = request_json['data']['quiz']
#         options = request_json['data']['options']
#         _question = question
#         _options = options.copy()
#         print(_options)
#
#
#     elif path == 2:
#
#         answer_option = request_json['data']['num']
#
#         answer = _options[int(answer_option)-1]
#         print(answer)
#
# cat_test(1)

c = [-10,-5,0,5,3,10,15,-20,25]

print (c.index(min(c)))  # 返回最小值
print (c.index(max(c))) # 返回最大值