# -*- coding: utf-8 -*-
__author__ = 'Allen'

import json,os
from mitmproxy import ctx
from urllib.parse import quote
import string
import requests
from db_repository import get_answer_from_db,insert_question
from adb_tools import auto_click


_question = ''
_options = []



def response(flow):
    path = flow.request.path
    global _question
    global _options
    if path == '/question/bat/findQuiz':
        data = json.loads(flow.response.text)
        question = data['data']['quiz']
        options = data['data']['options']
        _question = question
        _options = options.copy()
        ctx.log.info('question : %s, options : %s'%(question, options))
        option_position = get_answer(question, options)
        ctx.log.info('qoption_position : %s' % (option_position))
        url_str = "http://localhost:5050/?option={0}".format(option_position)
        requests.get(url=url_str)
        # auto_click(option_position)
        # flow.response.text = json.dumps(data)
    elif path == '/question/bat/choose':
        data = json.loads(flow.response.text)
        answer_option = data['data']['answer']
        answer = _options[int(answer_option)-1]
        ctx.log.info('answer_option : %s, answer : %s' % (answer_option, answer))
        insert_question(_question,answer)
    elif path == '/question/bat/fightResult':
        import time
        time.sleep(1)
        url_str = "http://localhost:5050/?option=continue"
        requests.get(url=url_str)

def get_answer(question, options):
    db_result = get_answer_from_db(question)
    ctx.log.info("db_result:%s" %(db_result))
    if  db_result != None:
        ctx.log.info("bingo!there is an answer in database.")
        for i in range(len(options)):
            if db_result == options[i]:
                return "option"+str(i)
    else:
        ctx.log.info("no answer in database,then we search from baidu...")
        answer = search_from_net(question, options)
    return answer



def search_from_net(question, options):
    url = quote('https://www.baidu.com/s?wd=' + question, safe = string.printable)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    
    content = requests.get(url, headers=headers).text
    answer_count = []
    for option in options:
        count = content.count(option)
        ctx.log.info('option : %s, count : %s'%(option, count))
        answer_count.append(count)

    min_index = answer_count.index(min(answer_count))
    max_index = answer_count.index(max(answer_count))
    if '不' in question:
        return "option"+str(min_index)
    return "option"+str(max_index)


def adb_shell_choose():
    pass


def adb_shell_next():
    pass


