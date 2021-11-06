import json
from oauthData import  oauthdata
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


genre_list = [genre for genre in api.genres.GET() if genre["kind"] == "anime"]
genre_list.sort(key=sort_key)
genres = {}

for genre in genre_list:
    genres[genre['name']] = genre['id']
print(genres)
#
# print(genre_list)

# input("Choose genre: ")

response = api.animes.GET(order='ranked', limit=8)

for title in response:
    print(title["russian"])

# print(response)
