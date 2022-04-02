
messenger = {
    'chat': {
        'user': ['name1', 'name2'],
        'messages': [{
            'message': str,
        }]
    },
    'chat2': {
        'user': ['name2', 'name3'],
        'messages': [{
            'message': str,
        }]
    },
    'chat_group': [],
}


messenger['chat']['messages'].append('bbb')

def add_user_in_chat(user_name: str) -> None:
   messenger['chat']['user'].append(user_name)

def find_word(word: str):
   if word in messenger['chat']['messages']:
       print(f'{word} is found!')

def shared_chat(users: list, chat: str):
    for i in range(len(users)):
        if users[i] in messenger[chat]['user']:
           messenger['chat_group'].append(users[i])
    return messenger['chat_group']

g1 = shared_chat(['name2', 'name3'], 'chat2')
messenger['chat_group'] = []
print(g1, 'chat2')
g2 = shared_chat(['name1', 'name2'], 'chat')
print(g2, 'chat1')
