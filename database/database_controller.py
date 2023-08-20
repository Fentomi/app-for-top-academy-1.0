import json

class Database():
    def __init__(self):
        self.path = r'database/database.json'
        self.indent_for_json = 4

    def db_reset(self) -> None:
        with open(self.path, 'w', encoding='utf-8') as json_writer:
            write = {
                'users': {
                    'login': ['admin'],
                    'password': ['admin'],
                    'access': ['admin']
                },
                'learn': {
                    'learntype': [],
                    'learntime': []
                }
            }
            json_writer.write(json.dumps(write))
    #действия с пользователями
    def create_user(self, login: str, password: str, access: str) -> None:
        with open(self.path, 'r', encoding='utf-8') as json_reader:
            db = json.load(json_reader)
            with open(self.path, 'w', encoding='utf-8') as json_writer:
                db['users']['login'].append(login)
                db['users']['password'].append(password)
                db['users']['access'].append(access)

                db = json.dumps(db, indent=self.indent_for_json)
                json_writer.write(db)
    def delete_user(self, login: str) -> None:
        with open(self.path, 'r', encoding='utf-8') as json_reader:
            db = json.load(json_reader)
            with open(self.path, 'w', encoding='utf-8') as json_writer:
                for i in range(len(db['users']['login'])):
                    if login == db['users']['login'][i]:
                        db['users']['login'].pop(i)
                        db['users']['password'].pop(i)
                        db['users']['access'].pop(i)

                db = json.dumps(db, indent=self.indent_for_json)
                json_writer.write(db)
    def find_user(self, enter_login: str, enter_password):
        with open(self.path, 'r', encoding='utf-8') as json_reader:
            db = json.load(json_reader)
            for i in range(len(db['users']['login'])):
                if enter_login == db['users']['login'][i] and enter_password == db['users']['password'][i]:
                    return True, db['users']['access'][i]
            return False, 'Неверный логин или пароль'
    def show_users(self) -> None:
        with open(self.path, 'r', encoding='utf-8') as json_reader:
            db = json.load(json_reader)
        for i in range(len(db['users']['login'])):
            print(f"{i+1} пользователь: (login: {db['users']['login'][i]}) (password: {db['users']['password'][i]}) (access: {db['users']['access'][i]})")
    #получить словарь базы данных
    def get_database(self) -> dict:
        with open(self.path, 'r', encoding='utf-8') as json_reader:
            return json.load(json_reader)
    #действия с типами обучения
    def create_learntype(self, learntype: str):
        with open(self.path, 'r', encoding='utf-8') as json_reader:
            db = json.load(json_reader)
            with open(self.path, 'w', encoding='utf-8') as json_writer:
                db['learn']['learntype'].append(learntype)
                db = json.dumps(db, indent=self.indent_for_json)
                json_writer.write(db)
    def delete_learntype(self, learntype: str):
        with open(self.path, 'r', encoding='utf-8') as json_reader:
            db = json.load(json_reader)
            with open(self.path, 'w', encoding='utf-8') as json_writer:
                index = db['learn']['learntype'].index(learntype)
                db['learn']['learntype'].pop(index)
                db = json.dumps(db, indent=self.indent_for_json)
                json_writer.write(db)
    def get_current_learntypedata(self) -> list:
        data = self.get_database()['learn']['learntype']
        return data
def main():
    db = Database()
    db.path = r'database.json'


if __name__ == '__main__':
    main()