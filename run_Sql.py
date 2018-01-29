# -*- coding: utf-8 -*-
__author__ = 'Allen'

import sqlite3

def create_db():
    '''创建数据库存储问题及答案'''
    conn = sqlite3.connect("brain_mster_questions.db")
    cursor = conn.cursor()
    print("connect database named brain_mster_questions")
    try:
        cursor.execute("CREATE TABLE BM_QUESTIONS(ID INTEGER PRIMARY KEY ,QUESTION TEXT UNIQUE,ANSWER TEXT NOT NULL);")
        print("create table named BM_QUESTIONS")
    except Exception as e:
        print(e)
        print("create table failed,perhaps it already exists.")
    finally:
        cursor.close()
        conn.close()

def insert_test_data():
    '''将问题及答案插入数据库'''
    conn = sqlite3.connect("brain_mster_questions.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO BM_QUESTIONS(QUESTION,ANSWER) VALUES ('我是谁?','allen')")
        cursor.execute("INSERT INTO BM_QUESTIONS(QUESTION,ANSWER) VALUES ('我从哪里来?','天堂')")
        cursor.execute("INSERT INTO BM_QUESTIONS(QUESTION,ANSWER) VALUES ('我要到哪里去?','地狱')")
        conn.commit()
    except Exception as e:
        print(e,"insert data failed!")
    finally:
        cursor.close()
        conn.close()

# create_db()
insert_test_data()
