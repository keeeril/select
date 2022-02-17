create table if not exists Artist (
	artist_id serial primary key,
	artist_name varchar(40) unique not null
	);

create table if not exists Genre (
	genre_id serial primary key,
	genre_name varchar(40) unique not null
	);
	
create table if not exists Genre_Artist (
	artist_id integer references Artist(artist_id),
	genre_id integer references Genre(genre_id),
	constraint pk primary key (artist_id, genre_id)
	);
	
create table if not exists Albums (
	album_id serial primary key,
	album_name varchar(120) unique not null,
	releaseYear integer not null check (releaseYear>0)
	);
	
create table if not exists Albums_Artist (
	artist_id integer references Artist(artist_id),
	album_id integer references Albums(album_id),
	constraint pk1 primary key (artist_id, album_id)
	);
	
create table if not exists Tracks (
	track_id serial primary key,
	title varchar(400) unique not null,
	duration integer not null check (duration>0),
	album_id integer references Albums(album_id)
	);
	
create table if not exists Collection (
	collection_id serial primary key,
	collection_name varchar(120) unique not null,
	releaseYear integer not null check (releaseYear>0)
	);
	
create table if not exists Albums_collection (
	track_id integer references Tracks(track_id),
	collection_id integer references Collection(collection_id),
	constraint pk2 primary key (track_id, collection_id)
	);