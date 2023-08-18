import json

class Database():
    def create_user(self, login: str, password: str, access: str) -> None:
        with open('users.json', 'r', encoding='utf-8') as json_reader:
            db = json.load(json_reader)
            with open('users.json', 'w', encoding='utf-8') as json_writer:
                db['users']['login'].append(login)
                db['users']['password'].append(password)
                db['users']['access'].append(access)

                db = json.dumps(db, indent=2)
                json_writer.write(db)

    def delete_user(self, login: str) -> None:
        with open('users.json', 'r', encoding='utf-8') as json_reader:
            db = json.load(json_reader)
            with open('users.json', 'w', encoding='utf-8') as json_writer:
                for i in range(len(db['users']['login'])):
                    if login == db['users']['login'][i]:
                        db['users']['login'].pop(i)
                        db['users']['password'].pop(i)
                        db['users']['access'].pop(i)

                db = json.dumps(db, indent=2)
                json_writer.write(db)

    def find_user(self, enter_login: str, enter_password):
        with open('users.json', 'r', encoding='utf-8') as json_reader:
            db = json.load(json_reader)
            for i in range(len(db['users']['login'])):
                if enter_login == db['users']['login'][i] and enter_password == db['users']['password'][i]:
                    return True, db['users']['access'][i]
            return False, 'Неверный логин или пароль'

    def get_database(self) -> str:
        with open('users.json', 'r', encoding='utf-8') as json_reader:
            return json.load(json_reader)

    def show_users(self):
        with open('users.json', 'r', encoding='utf-8') as json_reader:
            db = json.load(json_reader)
        for i in range(len(db['users']['login'])):
            print(f"{i+1} пользователь: (login: {db['users']['login'][i]}) (password: {db['users']['password'][i]}) (access: {db['users']['access'][i]})")
def main():
    db = Database()

if __name__ == '__main__':
    main()