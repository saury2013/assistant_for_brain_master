# -*- coding: utf-8 -*-
__author__ = 'Allen'

import json
from mitmproxy import ctx
from urllib.parse import quote
import string
import requests
from db_repository import get_answer_from_db,insert_question


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
        fixed_options = get_answer(question, options)
        data['data']['options'] = fixed_options
        flow.response.text = json.dumps(data)
    elif path == '/question/bat/choose':
        data = json.loads(flow.response.text)
        answer_option = data['data']['answer']
        answer = _options[int(answer_option)-1]
        ctx.log.info('answer_option : %s, answer : %s' % (answer_option, answer))
        insert_question(_question,answer)

def get_answer(question, options):
    db_result = get_answer_from_db(question)
    ctx.log.info("db_result:%s" %(db_result))
    if  db_result != None:
        ctx.log.info("bingo!there is an answer in database.")
        answer = []
        for option in options:
            if db_result == option:
                answer.append(option+'[right]')
            else:
                answer.append(option)
    else:
        ctx.log.info("no answer in database,then we search from baidu...")
        answer = search_from_net(question, options)
    return answer



def search_from_net(question, options):
    url = quote('https://www.baidu.com/s?wd=' + question, safe = string.printable)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    
    content = requests.get(url, headers=headers).text
    answer = []
    for option in options:
        count = content.count(option)
        ctx.log.info('option : %s, count : %s'%(option, count))
        answer.append(option + ' [' + str(count) + ']')
    return answer

def adb_shell_choose():
    pass


def adb_shell_next():
    pass


