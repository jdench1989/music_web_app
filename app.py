from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
from lib.artist import Artist
from lib.database_connection import get_flask_database_connection
import os
from flask import Flask, request, Response

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/albums', methods=['GET'])
def get_all_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return "\n".join([f"{album}" for album in albums])

@app.route('/albums', methods=['POST'])
def create_album():
    if not all(key in request.form for key in ['title', 'release_year', 'artist_id']):
        return "Must include album title, release_year and artist id.", 400
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    repository.create(title, release_year, artist_id)
    return "", 200

@app.route('/artists', methods=['GET'])
def get_all_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    return ", ".join([f"{artist.name}" for artist in artists])
    
@app.route('/artists', methods=["POST"])
def create_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    name = request.form['name']
    genre = request.form['genre']
    artist = Artist(None, name, genre)
    repository.create(artist)
    return Response(status=200)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

