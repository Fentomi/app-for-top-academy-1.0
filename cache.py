write = {
                'users': {
                    'login': ['admin'],
                    'password': ['admin'],
                    'access': ['admin']
                },
                'learn': {
                    'learntype': [{
                        'name': '',
                        'learntime': []
                    },
                    {
                        'name': '',
                        'learntime': []
                    }
                    ]
                }
            }
list1 = write['learn']['learntype']
for item in list1:
    item['learntime'] = 29
print(list1)