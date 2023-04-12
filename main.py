import requests
import time

data = {
	"content": "@everyone https://discord.gg/GG5YdsZD98",
	"embeds": None,
	"username": "Δ team",
	"avatar_url": "https://thisisignitedoreo.github.io/delta.png",
	"attachments": []
}

while True:
	requests.post("https://discord.com/api/webhooks/1095798254978994187/oLuPuo0H8ST265I-y6yDJVS7ewieQr8jbx2rw8XbKwRFlImY63cMZ3EMRVeZ3xj6O3pA", json=data)
	time.sleep(2)
