# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Album(models.Model):
    album_id = models.CharField(max_length=36, primary_key=True)
    album_name = models.CharField(max_length=135)

    def __unicode__(self):
        return u"%s" % self.album_name

    class Meta:
        db_table = 'album_tbl'

class Artist(models.Model):
    artist_id = models.CharField(max_length=36, primary_key=True)
    artist_name = models.CharField(max_length=135)

    def __unicode__(self):
        return u"%s" % self.album_name

    class Meta:
        db_table = 'artist_tbl'

class Genre(models.Model):
    genre_id = models.CharField(max_length=36, primary_key=True)
    genre_name = models.CharField(max_length=135)

    def __unicode__(self):
        return u"%s" % self.album_name

    class Meta:
        db_table = 'genre_tbl'

class ReleaseLbl(models.Model):
    release_lbl_id = models.CharField(max_length=36, primary_key=True)
    release_lbl_name = models.CharField(max_length=135)

    class Meta:
        db_table = 'release_lbl_tbl'

class Track(models.Model):
    track_id = models.CharField(max_length=36, primary_key=True)
    track_name = models.CharField(max_length=135)

    def __unicode__(self):
        return u"%s" % self.track_name

    class Meta:
        db_table = 'track_id'

class MasterDb(models.Model):
    song_id = models.CharField(max_length=36, primary_key=True)
    song_name = models.CharField(max_length=135)
    artist = models.ForeignKey(Artist)
    track = models.ForeignKey(Track)
    album = models.ForeignKey(Album)
    release_year = models.CharField(max_length=12)
    release_lbl = models.ForeignKey(ReleaseLbl)
    genre = models.ForeignKey(Genre)
    download_times = models.IntegerField()

    def __unicode__(self):
        return u"%s" % self.track + "by" + u"%s" % self.artist

    class Meta:
        db_table = 'master_db'


class UserCredentials(models.Model):
    user_id = models.CharField(max_length=36, primary_key=True)
    password = models.CharField(max_length=75)

    class Meta:
        db_table = 'user_credentials'

class UserPlaylist(models.Model):
    user = models.ForeignKey(UserCredentials)
    pl_id = models.CharField(max_length=36, unique=True)
    pl_name = models.CharField(max_length=135)

    def __str__(self):
        return self.pl_id

    class Meta:
        db_table = 'user_playlist'


