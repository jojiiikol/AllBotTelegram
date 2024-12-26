# from requests import request
# from bs4 import BeautifulSoup
#
# emotion_list = []
#
# req = request(url="https://emojidb.org/ascii-emoticons-emojis", method="GET")
# bs = BeautifulSoup(req.text, "html.parser")
# emotion_table = bs.find("div", {"class": "emoji-list"})
# emotions = emotion_table.find_all("div", {"class": "emoji-ctn"})
# for emotion in emotions:
#     emotion_list.append(emotion.find("div", {"class": "emoji"}).text)
#
# print(emotion_list)
from pyrogram import Client

api_id = 20938959
api_hash = "a89d86800a67d0bb407f8aebecedb1eb"
app = Client("ChDBBot", api_id, api_hash)

async def baba():
    async with app:
        async for dialog in app.get_dialogs():
            print(dialog.chat.title or dialog.chat.first_name)

app.run(baba())

