import json

import requests

from oauthData import oauthdata
from shikimori_api import Shikimori


def token_saver(token: dict):
    with open('token.json', 'w') as f:
        f.write(json.dumps(token))


# session = Shikimori('disBotAnimeHelper', client_id=oauthdata["client_id"], client_secret=oauthdata["client_secret"],
#                     token_saver=token_saver)
#
# print(session.get_auth_url())
# code = input('Authorization Code: ')
# session.fetch_token(code)

def sort_key(genres: dict):
    return genres["id"]


with open('token.json') as f:
    token = json.load(f)
session = Shikimori('disBotAnimeHelper', client_id=oauthdata["client_id"], client_secret=oauthdata["client_secret"],
                    token=token, token_saver=token_saver)
api = session.get_api()


def get_genres_list():
    genre_list = [genre for genre in api.genres.GET() if genre["kind"] == "anime"]
    genre_list.sort(key=sort_key)
    genres = {}
    stringr = ""

    for genre in genre_list:
        genres[genre['name']] = genre['id']
    count = 1
    for genre in genres:
        genr = (str(count) + ". " + genre + "\n")
        stringr += genr
        count = count + 1
    return stringr


def anime_list():
    animeList = []
    stringr = ""
    response = api.animes.GET(order="random",limit=10)
    # print(response)
    for title in response:
        if not title["russian"]:
            animeList.append(title["name"])
        else:
            animeList.append(title["russian"])
    count = 1
    for names in animeList:
        anime = (str(count) + ". " + names + "\n")
        stringr += anime
        count = count + 1
    return stringr

