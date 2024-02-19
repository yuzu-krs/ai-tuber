from pychatgpt import Chat, Options

options = Options()

options.track = True

options.chat_log = "chat_log.txt"
options.id_log = "id_log.txt"

chat = Chat(email="yuzuto.poi@gmail.com", password="Yuzuto13@/stoit", options=options)
chat.cli_chat()