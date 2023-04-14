import requests
import json

headers = {'Content-type': 'application/json'}

def token_from_login(login: str, password: str) -> tuple:
	"""Get token from login and password
	YOUR PASSWORD OR LOGIN IS NOT STORED ANYWHERE,
	IT'S USED JUST FOR LOGIN!"""
	r = requests.post("https://canary.discord.com/api/v10/auth/login", json={"login": login, "password": password}, headers=headers)
	resp = json.loads(r.text)
	print(r.text)
	return resp["token"], resp["user_id"]

def get_guilds(token: str) -> list:
	"""Get list of joined servers"""
	return json.loads(requests.get(f"https://canary.discord.com/api/v10/users/@me/guilds?token={token}").content)

def get_guild_channels(token: str, guild_id: int) -> list:
	"""Get list of channels of server (you must be joined in)"""
	return json.loads(requests.get(f"https://canary.discord.com/api/v10/guilds/{guild_id}/channels?token={token}").content)

def get_channel_messages(token: str, channel_id: int, limit: int=50) -> list:
	"""Get list of channels of server (you must be joined in)"""
	return json.loads(requests.get(f"https://canary.discord.com/api/v10/channels/{channel_id}/messages?token={token}&limit={limit}").content)

def send_message(token: str, channel_id: int, content: str) -> None:
	return json.loads(requests.post(f"https://discordapp.com/api/channels/{channel_id}/messages", json={"content": content}, headers={"Content-Type": "application/json", "Authorization": token}).content)

if __name__ == '__main__':
	send_message("NzUwMzMyNzQwMDY2NDc2MDY0.Gwm_qv.6pAb73-3zPOiT0HdAGmBIoaSXLUzjYDud2n0Jk", 965599615862841405, ":)")
