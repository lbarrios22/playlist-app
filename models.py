from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    app.app_context().push()


class Playlist(db.Model):
    '''Makes a Playlist Model'''

    __tablename__ = 'playlists'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(10), nullable=False)

    description = db.Column(db.String(30))

    songs = db.relationship('Song', secondary='playlists_songs', backref='playlists')

class PlaylistSong(db.Model):
    '''Makes a model PlaylistSong Model and it takes the foreign key of playlists.id and songs.id'''

    __tablename__ = 'playlists_songs'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'))

    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'))


class Song(db.Model):
    '''Makes a model to add songs'''

    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    title = db.Column(db.String(10), nullable=False)

    artist = db.Column(db.String(10), nullable=False)