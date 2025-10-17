import time
import random
import requests
import utils

CHANNELID = 1371020652227592255
TOKEN = ""
DELAY = 3

for i in range(200):
    result = ""
    for i in range(5):
        result += random.choice(utils.first)+random.choice(utils.second)
    result = utils.retarded(result, utils.divideHangul)
    requests.post(f"https://discord.com/api/v10/channels/{CHANNELID}/messages", headers={"Authorization": TOKEN, "Content-Type": "application/json"}, json={"content": "# "+result})
    time.sleep(DELAY)