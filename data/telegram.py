import os
import json


def get_text():
    text = []

    for filename in os.listdir(os.path.join(os.getcwd(), 'data/telegram')):
        with open(os.path.join(os.getcwd(), f'data/telegram/{filename}'), 'r') as f:  # open in readonly mode
            try:
                data = json.load(f)
            except:
                continue

            for obj in data:
                try:
                    text.append(obj['message'])
                except:
                    pass

    return text


def get_details_text():
    text = []

    for filename in os.listdir(os.path.join(os.getcwd(), 'data/telegram')):
        with open(os.path.join(os.getcwd(), f'data/telegram/{filename}'), 'r') as f:  # open in readonly mode
            try:
                data = json.load(f)
            except:
                continue

            for obj in data:
                try:
                    text.append((obj['message'], obj['date'], None))
                except:
                    pass

    return text


def splitFile():
    file1 = []
    file2 = []
    for filename in os.listdir(os.path.join(os.getcwd(), 'data/telegram')):
        with open(os.path.join(os.getcwd(), f'data/telegram/{filename}'), 'r') as f:  # open in readonly mode
            try:
                data = json.load(f)
            except:
                continue

            for i, obj in enumerate(data):
                print(f.__sizeof__())
                try:
                    if i < len(data) / 2:
                        file1.append(obj)
                    else:
                        file2.append(obj)

                except:
                    pass

        with open(os.path.join(os.getcwd(), f'data/telegram/{filename}1.json'), 'w') as f:
            for d in file1:
                f.write(str(d))

        with open(os.path.join(os.getcwd(), f'data/telegram/{filename}2.json'), 'w') as f:
            for d in file2:
                f.write(str(d))

