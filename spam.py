import discord_api
import time

token = open("saved_token.txt").read()

n = 0
while True:
    n += 1
    print("total:", n, end="\r")
    returned = discord_api.send_message(token, "1059051473503273010", "слушай, ну не плохо стерва")
    if "message" in returned.keys():
        print("\n" + returned["message"])
        exit()
    # returned = discord_api.send_message(token, "1093866026376122441", "слушай, ну не плохо стерва")
    # if "message" in returned.keys():
    #     print("\n" + returned["message"])
    #     exit()
    time.sleep(5)
