from models import Playlist, PlaylistSong, Song, db
from app import app

app.app_context

db.drop_all()
db.create_all()

playlist1 = Playlist(name='Playlist 1', description='Sample playlist 1')
playlist2 = Playlist(name='Playlist 2', description='Sample playlist 2')
playlist3 = Playlist(name='Playlist 3', description='Sample playlist 3')

db.session.add_all([
    playlist1, 
    playlist2, 
    playlist3,
])
db.session.commit()


song1 = Song(title='Song 1', artist='Artist 1')
song2 = Song(title='Song 2', artist='Artist 2')
song3 = Song(title='Song 3', artist='Artist 3')

db.session.add_all([
    song1, 
    song2, 
    song3,
])
db.session.commit()

playlist_song1 = PlaylistSong(playlist_id=1, song_id=1)
playlist_song2 = PlaylistSong(playlist_id=1, song_id=2)
playlist_song3 = PlaylistSong(playlist_id=2, song_id=3)

db.session.add_all([
    playlist_song1, 
    playlist_song2, 
    playlist_song3
])
db.session.commit()
