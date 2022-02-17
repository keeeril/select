import sqlalchemy
import json

with open("PlaylistExport.json", "r", encoding="utf-8") as file:
    data = json.load(file)

for i in data:
    del i["platform"]
    del i["id"]
    del i["artistLink"]
    del i["albumLink"]
    del i["isrc"]
    del i["trackLink"]
    del i["position"]
    del i["shareUrls"]

with open("PlaylistExport2.json", "w", encoding="utf-8") as file:
        json.dump(data, file)

with open("PlaylistExport2.json", "r", encoding="utf-8") as file:
    data = json.load(file)

engine = sqlalchemy.create_engine('postgresql://kir:1111@localhost:5432/music_test')
connection = engine.connect()

artists = []
for one_artist in data:
    artists.append(one_artist['artist'])

genres = []
for one_genre in data:
    genres.append((one_genre['genre']))

for artist in set(artists):
    connection.execute(f"INSERT INTO artist(artist_name) VALUES('{artist}')")
sel_art = connection.execute("""SELECT * FROM artist;""").fetchall()

for genre in set(genres):
    connection.execute(f"INSERT INTO genre(genre_name) VALUES('{genre}')")
sel_gen = connection.execute("""SELECT * FROM genre;""").fetchall()

sel = connection.execute("""SELECT * FROM artist;""").fetchall()

sel1 = connection.execute("""SELECT * FROM genre;""").fetchall()

artgen = {}

for a in sel:
    for g in sel1:
        for index in data:
            if a[1] == index['artist'] and g[1] == index['genre']:
                artgen[a[0]] = g[0]

for art, gen in artgen.items():
    connection.execute(f"INSERT INTO genre_artist VALUES ({art}, {gen})")

albums = {}
for one_album in data:
    albums[one_album['album']] = one_album['addedDate']

new_albums = {}
for i, j in albums.items():
    if i not in new_albums.keys():
        new_albums[i] = j

for album, released in new_albums.items():
    connection.execute(f"INSERT INTO albums(album_name, releaseyear) VALUES('{album}', '{released}')")
sel_alb = connection.execute("""SELECT * FROM albums;""").fetchall()

albart = {}

for a in sel:
    for al in sel_alb:
        for index in data:
            if a[1] == index['artist'] and al[1] == index['album']:
                albart[a[0]] = al[0]

for arti, alb in albart.items():
    connection.execute(f"INSERT INTO albums_artist VALUES ({arti}, {alb})")

collection = {'Favourite': 2019, 'New': 2020, 'Old': 2015, 'Recently added': 2022}

for collectt, rel in collection.items():
    connection.execute(f"INSERT INTO collection(collection_name, releaseyear) VALUES('{collectt}', '{rel}')")
sel_collection = connection.execute("""SELECT * FROM collection;""").fetchall()

tracks = []
for index in data:
    tracks.append(index['title'])

track_albums = {}
for albb in sel_alb:
    for index in data:
        if albb[1] == index['album']:
            track_albums[index['title']] = albb[0]

for key, val in track_albums.items():
    connection.execute(f"INSERT INTO tracks(title, duration, album_id) VALUES('{key}', 4, '{val}')")

sel_track = connection.execute("""SELECT * FROM tracks;""").fetchall()

for n in sel_track:
    if n[0] in range(0,10):
        connection.execute(f"INSERT INTO albums_collection VALUES ({n[0]}, 1)")
    elif n[0] in range(10,22):
        connection.execute(f"INSERT INTO albums_collection VALUES ({n[0]}, 2)")
    elif n[0] in range(22,39):
        connection.execute(f"INSERT INTO albums_collection VALUES ({n[0]}, 3)")
    else:
        connection.execute(f"INSERT INTO albums_collection VALUES ({n[0]}, 4)")
