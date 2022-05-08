class Messenger:
    def __init__(self, chat:dict, messages:str, chat_group:list):
        self.chat = chat
        self.messages = messages

    def add_user_in_chat(self, chat_name: str, user_name: str) -> None:
        self.chat[chat_name].append(user_name)
        # print(self.chat)

    def find_word(self, word: str):
        if word in self.messages:
           print(f'{word} is found!')
        else:
            print(f'{word} is Not found!')


messeng = Messenger({'ch1': ['Bob','Alice'], 'ch2':'Katrin', 'ch3': 'John'}, 'hello world!', ['family chat', 'work chat'])
messeng.add_user_in_chat('ch1', 'Alua')
messeng.find_word('dog')

