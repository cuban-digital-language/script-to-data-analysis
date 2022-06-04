from submodulos.tokenizer.custom_tokenizer import SpacyCustomTokenizer
from tools import get_progressbar
from word_db import WordDB
from concurrent.futures import ThreadPoolExecutor
from pyrae import dle
from time import sleep
from redis import Redis
import ast
from submodulos.data import tw as data
import sys
import os


def count():
    word_db = WordDB(localhost='localhost', port=6379, db=2)

    count = 0
    for obj in word_db:
        if obj is None or not 'rae' in obj:
            count += 1

    print(f"from {len(word_db)} words not requested {count}")


def find():
    word_db = Redis(host='localhost', port=6379, db=2)
    a = word_db.keys()

    def get_word():
        for word in word_db.keys():
            # word = word.decode().lower()
            word_obj = ast.literal_eval(word_db.get(word).decode())

            if word_obj is None or not 'rae' in word_obj:
                yield word, word_obj if not word_obj is None else {}

    pool = ThreadPoolExecutor()
    ort_error = []

    def fun(word, word_obj):
        word_in_rae = dle.search_by_word(word)
        word_obj["rae"] = word_in_rae.to_dict()
        word_db.set(word, str(word_obj))
        # if a.title.startswith("Diccionario de la lengua española"):
        #     ort_error.append(word)

    for word, obj in get_word():
        pool.submit(fun, word, obj)
        sleep(60)


def save():

    # import data.cubadebate as cb

    text = data.get_text(f'{os.getcwd()}/submodulos/data/')

    word_db = WordDB(localhost='localhost', port=6379, db=2)
    nlp = SpacyCustomTokenizer()
    bar = get_progressbar(
        len(text), f' from {len(text)} text, get work for RAE checked ')
    bar.start()
    count = 0
    for i, t in enumerate(text):
        t, _ = t
        for token in nlp(t):
            if not token.natural_word():
                continue
            count += word_db.try_save(token.text.lower(), {})

        bar.update(i + 1)
    bar.finish()

    print(f'${count} new words')


cmd = sys.argv[1]

if cmd == count.__name__:
    print('count command')
    count()

if cmd == save.__name__:
    print('save command')
    save()

if cmd == find.__name__:
    print('find command')
    find()
