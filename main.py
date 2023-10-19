from webserver import keep_alive
import requests

channelID = 1163946470697877625
headers = {
    "authorization":
    "MTEzNjc3Nzg2NDIyNjgwNzg2OQ.GHsoAe.sCYOnlJjtIUBo4seov5kQFujjDHH8YEsfCDY7E"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
