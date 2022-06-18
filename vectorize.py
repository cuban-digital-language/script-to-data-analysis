from submodulos.tokenizer.custom_tokenizer import SpacyCustomTokenizer, get_progressbar
from submodulos.data import get_all_text
import sys
import os
import ast


def word():
    bar = get_progressbar(len(texts), ' Tokenizer ')
    bar.start()
    for i, text in enumerate(texts):
        for _ in nlp(text[0]):
            pass
        bar.update(i+1)
    bar.finish()

    bar = get_progressbar(len(nlp.embedding), ' Save ')
    bar.start()
    i = 0
    for key, value in nlp.embedding.items():
        with open(f'results/words/{hash(key)}.txt', 'w+') as f:
            f.write(str((key, value)))
            f.close()

        i += 1
        bar.update(i)
    bar.finish()


def tokens():
    bar = get_progressbar(len(texts), ' Tokenizer ')
    bar.start()
    for i, text in enumerate(texts):
        for _ in nlp(text[0]):
            pass
        bar.update(i+1)
    bar.finish()

    bar = get_progressbar(len(texts), ' Save ')
    bar.start()
    i = 0
    for t, _ in texts:
        hsh = hash(t)
        with open(f'results/tokens/{hsh}.txt', 'w+') as f:
            f.write(str((t, nlp.memory[str(hsh)])))
            f.close()

        i += 1
        bar.update(i)
    bar.finish()


def length(type):
    return len(os.listdir(f'results/{type}'))


def load(type='words'):
    for filename in os.listdir(f'results/{type}'):
        with open(f'results/{type}/{filename}', 'r') as f:
            text = f.read()
            f.close()
            yield ast.literal_eval(text)


def sent():
    bar = get_progressbar(len(texts), ' Tokenizer ')
    bar.start()
    embedding = {}
    for i, text in enumerate(texts):
        for token in nlp.nlp(text[0]).sents:
            embedding[token.text] = tuple(token.vector)
        bar.update(i+1)
    bar.finish()

    bar = get_progressbar(len(embedding), ' Save ')
    bar.start()
    i = 0
    for key, value in embedding.items():
        with open(f'results/sentences/{hash(key)}.txt', 'w+') as f:
            f.write(str((key, value)))
            f.close()

        i += 1
        bar.update(i)
    bar.finish()


def text():
    bar = get_progressbar(len(texts), ' Tokenizer ')
    bar.start()
    embedding = {}
    for i, text in enumerate(texts):
        embedding[text[0]] = tuple(nlp.nlp(text[0]).vector)
        bar.update(i+1)
    bar.finish()

    bar = get_progressbar(len(texts), ' Save ')
    bar.start()
    i = 0
    for key, value in embedding.items():
        with open(f'results/texts/{hash(key)}.txt', 'w+') as f:
            f.write(str((key, value)))
            f.close()
        i += 1
        bar.update(i)
    bar.finish()


if __name__ == '__main__':
    texts = get_all_text('submodulos/data/')
    nlp = SpacyCustomTokenizer()

    cmd = sys.argv[1]

    if cmd == word.__name__:
        print('word command')
        word()

    if cmd == tokens.__name__:
        print('tokens command')
        tokens()

    if cmd == sent.__name__:
        print('sent command')
        sent()

    if cmd == text.__name__:
        print('text command')
        text()
