import json

class Database():
    def create_user(self, login: str, password: str, access: str) -> None:
        with open('database/users.json', 'r', encoding='utf-8') as json_reader:
            db = json.load(json_reader)
            with open('database/users.json', 'w', encoding='utf-8') as json_writer:
                db['users']['login'].append(login)
                db['users']['password'].append(password)
                db['users']['access'].append(access)

                db = json.dumps(db)
                json_writer.write(db)

    def delete_user(self, login: str) -> None:
        with open('database/users.json', 'r', encoding='utf-8') as json_reader:
            db = json.load(json_reader)
            with open('database/users.json', 'w', encoding='utf-8') as json_writer:
                for i in range(len(db['users']['login'])):
                    if login == db['users']['login'][i]:
                        db['users']['login'].pop(i)
                        db['users']['password'].pop(i)
                        db['users']['access'].pop(i)

                db = json.dumps(db)
                json_writer.write(db)

    def find_user(self, enter_login: str, enter_password):
        with open('database/users.json', 'r', encoding='utf-8') as json_reader:
            db = json.load(json_reader)
            for i in range(len(db['users']['login'])):
                if enter_login == db['users']['login'][i] and enter_password == db['users']['password'][i]:
                    return True, db['users']['access'][i]
            return False, 'Неверный логин или пароль'

    def get_database(self) -> str:
        with open('database/users.json', 'r', encoding='utf-8') as json_reader:
            return json.load(json_reader)