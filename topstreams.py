import requests
import json
import locale
from dotenv import load_dotenv
import os

locale.setlocale(locale.LC_ALL, 'en_US')
load_dotenv()


def get_game(game_id):
	"""Get the games being played by the top streamers"""
	url =  "https://api.twitch.tv/helix/games?id=" + str(game_id)
	game = requests.get(url, headers={
		"Client-ID": os.getenv("C_ID"),
		"Authorization": os.getenv("Auth")
	})
	game_body = json.loads(game.text)
	for g in game_body['data']:
		return g['name']

def get_topStreams():	
	"""Get the top streamers on twitch"""
	url = 'https://api.twitch.tv/helix/streams?first=10'
	r = requests.get(url, headers={
		"Client-ID": os.getenv("C_ID"),
		"Authorization": os.getenv("Auth")
		})
	info_dict = json.loads(r.text)
	print("-"*35 + "Top Streamers" + "-"*35)
	print(f"{'Channel':<25} {'Viewers':<15} {'Game'}")
	for name in info_dict['data']:
		print(f"{name['user_name']:<25} {locale.format_string('%d',name['viewer_count'], grouping=True):<15} {get_game(name['game_id'])} \n")



def topGames():
	"""Get the first top 10 games"""
	url =  "https://api.twitch.tv/helix/games/top?first=10"
	games = requests.get(url, headers={
		"Client-ID": os.getenv("C_ID"),
		"Authorization": os.getenv("Auth")
	})
	top_games = json.loads(games.text)
	print("-"*15 + "Top Games" + "-"*15)
	for games in top_games['data']:
		print(games['name'])
	print("\n")

def twitchDriver():
	get_topStreams()
	topGames()

if __name__ == "__main__":
	print("Starting...")
	twitchDriver()