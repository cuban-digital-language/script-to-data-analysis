from redis import Redis
import ast


class WordDB:
    def __init__(self, localhost, port, db) -> None:
        self.db = Redis(localhost, port, db)

    def get(self, text):
        obj = self.db.get(text)
        return ast.literal_eval(obj.decode()) if not obj is None else {}

    def save(self, text, obj):
        self.db.set(text, str(obj))

    def try_save(self, text, obj):
        obj = self.db.get(text)
        if obj is None:
            self.save(text, obj)
            return 1

        return 0

    def __iter__(self):
        for obj in self.db.mget(self.db.keys()):
            yield ast.literal_eval(obj.decode()) if not obj is None else {}

    def __len__(self):
        return len(self.db.keys())


if __name__ == '__main__':
    word_db = WordDB(localhost='localhost', port=6379, db=2)

    for key in word_db.db.keys():
        obj = word_db.db.get(key).decode()
        if obj == 'None':
            word_db.db.delete(key)
