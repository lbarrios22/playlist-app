from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import InputRequired, Length

class PlaylistForm(FlaskForm):
    '''Makes a form to add a playlist to db'''

    name = StringField('Playlist Name', validators=[InputRequired(), Length(max=10)])

    description = StringField('Description', validators=[Length(max=30)])

class SongForm(FlaskForm):
    '''Makes a form to add a song to db'''

    title = StringField('Song Name', validators=[InputRequired(), Length(max=10)])

    artist = StringField('Artist Name', validators=[InputRequired(), Length(max=10)])

class PlaylistSongForm(FlaskForm):
    '''Makes a form that gives specific song titles to add to the playlist'''

    title = SelectField('Song to add', validators=[InputRequired()])