import os
import json


def get_text():
    text = []

    for filename in os.listdir(os.path.join(os.getcwd(), 'data/telegram')):
        with open(os.path.join(os.getcwd(), f'data/telegram/{filename}'), 'r') as f: # open in readonly mode
            try: data = json.load(f)
            except: continue

            for obj in data:
                try: text.append(obj['message'])
                except: pass

    return text


def get_details_text():
    text = []

    for filename in os.listdir(os.path.join(os.getcwd(), 'data/telegram')):
        with open(os.path.join(os.getcwd(), f'data/telegram/{filename}'), 'r') as f: # open in readonly mode
            try: data = json.load(f)
            except: continue

            for obj in data:
                try: text.append((obj['message'], obj['date'], None))
                except: pass

    return text