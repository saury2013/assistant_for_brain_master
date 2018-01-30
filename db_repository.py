# -*- coding: utf-8 -*-
__author__ = 'Allen'

import sqlite3



def get_answer_from_db(question):
    conn = sqlite3.connect("brain_mster_questions.db")
    result = None
    cursor = conn.cursor()
    sql_cmd = "SELECT ANSWER FROM BM_QUESTIONS WHERE QUESTION = ?"
    try:
        cursor.execute(sql_cmd,(question,))
        result = cursor.fetchone()[0]
        print(result)
    except Exception as e:
        print(e,"get_answer_from_db error")
    finally:
        cursor.close()
        conn.close()

    return result

def insert_question(question,answer):
    conn = sqlite3.connect("brain_mster_questions.db")
    cursor = conn.cursor()
    sql_cmd = "INSERT INTO BM_QUESTIONS(QUESTION,ANSWER) VALUES (?,?)"
    try:
        cursor.execute(sql_cmd,(question,answer))
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# get_answer_from_db("「侬」的意思是？")
# insert_question("中国的首都是什么地方?","beijing")