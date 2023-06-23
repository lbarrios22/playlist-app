from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, Playlist, PlaylistSong, Song
from forms import SongForm, PlaylistForm, PlaylistSongForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlist_db'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'sakdjhhslad324324'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def home_page():
    '''Redirects to playlists route'''
    return redirect('/playlists')

@app.route('/playlists')
def all_playlists():
    '''Renders template to show all playlists'''

    playlists = Playlist.query.all()

    return render_template('all_playlists.html', playlists=playlists)

@app.route('/playlists/<int:playlist_id>')
def show_playlist(playlist_id):
    '''Shows the specified playlist by id'''

    playlist = Playlist.query.get_or_404(playlist_id)

    return render_template('show_playlist.html', playlist=playlist)

@app.route('/playlists/add', methods=['GET', 'POST'])
def create_playlist():
    '''Shows form to create a playlist'''
    
    form = PlaylistForm()

    if form.validate_on_submit():
        name  = form.name.data
        description = form.description.data

        new_playlist = Playlist(name=name, description=description)

        db.session.add(new_playlist)
        db.session.commit()
        flash('Playlist Created!', 'success')

        return redirect('/playlists')
    else:
        return render_template('create_playlist.html', form=form)
    
@app.route('/songs')
def all_songs():
    '''Renders template to show all songs'''

    songs = Song.query.all()

    return render_template('all_songs.html', songs=songs)

@app.route('/songs/<int:song_id>')
def show_song(song_id):
    '''Shows specified song with the song id'''

    song = Song.query.get_or_404(song_id)

    return render_template('show_song.html', song=song)

@app.route('/songs/add', methods=['GET', 'POST'])
def add_song():
    '''Shows form to add a song'''

    form = SongForm()

    if form.validate_on_submit():
        title = form.title.data
        artist = form.artist.data

        new_song = Song(title=title, artist=artist)

        db.session.add(new_song)
        db.session.commit()

        flash('Song Added!', 'success')

        return redirect('/playlists')
    
    else:
        return render_template('add_song.html', form=form)
    
@app.route('/playlists/<int:playlist_id>/add-song', methods=['GET', 'POST'])
def add_song_to_playlist(playlist_id):
    '''Shows form to add songs to a specific playlist'''

    playlist = Playlist.query.get_or_404(playlist_id)
    form = PlaylistSongForm()
    in_playlist = [song.id for song in playlist.songs]
    songs_to_add = (db.session.query(Song.id, Song.title)
                      .filter(Song.id.notin_(in_playlist))
                      .all())
    form.title.choices = [(song.id, song.title) for song in songs_to_add]
    

    if form.validate_on_submit():
        new_song_in_playlist = PlaylistSong(playlist_id=playlist.id, song_id=form.title.data)

        db.session.add(new_song_in_playlist)
        db.session.commit()

        flash('Added song to playlist', 'success')
        return redirect(f'/playlists/{playlist_id}')
    else:
        return render_template('add_song_to_playlist.html', form=form, playlist=playlist)