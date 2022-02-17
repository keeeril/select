import sqlalchemy


engine = sqlalchemy.create_engine('postgresql://kir:1111@localhost:5432/music_test')
connection = engine.connect()

# 1
sel1 = connection.execute("""SELECT album_name, releaseyear FROM albums
    WHERE releaseyear = 2018""")

# 2
connection.execute("""SELECT title, duration FROM tracks
    ORDER BY duration DESC
    LIMIT 1""")

# 3
connection.execute("""SELECT title FROM tracks
    WHERE duration > 3.5""")

# 4
connection.execute("""SELECT collection_name FROM collection
    WHERE releaseyear BETWEEN 2018 AND 2020""")

# 5
connection.execute("""SELECT SPLIT_PART(artist_name, ' ', 1) FROM artist""")

# 6
connection.execute("""SELECT title FROM tracks
    WHERE title iLIKE '%%my%%' OR '%%мой%%'""")
