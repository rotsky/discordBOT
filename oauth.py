import json

import requests

from oauthData import oauthdata
from shikimori_api import Shikimori


def token_saver(token: dict):
    with open('token.json', 'w') as f:
        f.write(json.dumps(token))
    start_session()

# session = Shikimori('disBotAnimeHelper', client_id=oauthdata["client_id"], client_secret=oauthdata["client_secret"],
#                     token_saver=token_saver)
#
# print(session.get_auth_url())
# code = input('Authorization Code: ')
# session.fetch_token(code)

# def refresh_token():
#     url = "https://shikimori.one/oauth/token"
#     headers = {
#         "User-Agent": "disBotAnimeHelper"
#     }
#     params = {
#         "grant_type": "refresh_token",
#         "client_id": "2Hhz733lFDj5Dv4nhIfNzvltj2MgAnnlMp5rP837ni8",
#         "client_secret": "eBU7DVJiBdStP7tBCqW0LgTCSflC0zfnb7LVNmT_bB0",
#         "refresh_token": "plnPb4dG9Ucjjs9TfUsfAUy4_tJQzyzs_ItrgXU-cjU"
#     }
#     response = api.POST(url, headers=headers, data=params)
#     token_saver(response)
#
#
# def refresh():
#     url = "https://shikimori.one/oauth/token"
#     headers = {
#         "User-Agent": "disBotAnimeHelper"
#     }
#     params = {
#         "grant_type": "refresh_token",
#         "client_id": "2Hhz733lFDj5Dv4nhIfNzvltj2MgAnnlMp5rP837ni8",
#         "client_secret": "eBU7DVJiBdStP7tBCqW0LgTCSflC0zfnb7LVNmT_bB0",
#         "refresh_token": token['refresh_token']
#     }
#     response = requests.post(url=url, headers=headers, data=params)
#     print(response)
#     token_saver(response.json())

def sort_key(genres: dict):
    return genres["id"]


def start_session():
    with open('token.json') as f:
        token = json.load(f)
    session = Shikimori('disBotAnimeHelper', client_id=oauthdata["client_id"], client_secret=oauthdata["client_secret"],
                        token=token, token_saver=token_saver)
    api = session.get_api()
    return api


api = start_session()


def search_anime(stringr):
    anime_list = [anime for anime in api.animes.GET(search=stringr, limit=1) if anime['kind'] == 'tv']
    print(anime_list)
    return anime_list


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


def random_anime_list():
    animeList = []
    stringr = ""
    response = api.animes.GET(order="random")
    print(response)
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

