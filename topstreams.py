import requests
import json
import locale
import time
locale.setlocale(locale.LC_ALL, 'en_US')


def get_game(game_id):
	url =  "https://api.twitch.tv/helix/games?id=" + str(game_id)
	game = requests.get(url, headers={
	})
	game_body = json.loads(game.text)
	for g in game_body['data']:
		return g['name']

def get_topStreams():	
	url = 'https://api.twitch.tv/helix/streams?first=10'
	r = requests.get(url, headers={
		})
	info_dict = json.loads(r.text)

	for name in info_dict['data']:
		print("Channel: {c} \nViewers: {v} \nGame: {g}\n----------------------------".
		format(c = name['user_name'], v = locale.format("%d", name['viewer_count'], grouping=True), 
		g = get_game(name['game_id'])))

if __name__ == "__main__":
	print("Starting...")
	get_topStreams()