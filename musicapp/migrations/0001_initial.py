# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('album_id', models.CharField(serialize=False, primary_key=True, max_length=36)),
                ('album_name', models.CharField(max_length=135)),
            ],
            options={
                'db_table': 'album_tbl',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('artist_id', models.CharField(serialize=False, primary_key=True, max_length=36)),
                ('artist_name', models.CharField(max_length=135)),
            ],
            options={
                'db_table': 'artist_tbl',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('genre_id', models.CharField(serialize=False, primary_key=True, max_length=36)),
                ('genre_name', models.CharField(max_length=135)),
            ],
            options={
                'db_table': 'genre_tbl',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MasterDb',
            fields=[
                ('song_id', models.CharField(serialize=False, primary_key=True, max_length=36)),
                ('song_name', models.CharField(max_length=135)),
                ('release_year', models.CharField(max_length=12)),
                ('download_times', models.IntegerField()),
                ('album', models.ForeignKey(to='musicapp.Album')),
                ('artist', models.ForeignKey(to='musicapp.Artist')),
                ('genre', models.ForeignKey(to='musicapp.Genre')),
            ],
            options={
                'db_table': 'master_db',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlaylistEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
            ],
            options={
                'db_table': 'playlist_entry',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReleaseLbl',
            fields=[
                ('release_lbl_id', models.CharField(serialize=False, primary_key=True, max_length=36)),
                ('release_lbl_name', models.CharField(max_length=135)),
            ],
            options={
                'db_table': 'release_lbl_tbl',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('track_id', models.CharField(serialize=False, primary_key=True, max_length=36)),
                ('track_name', models.CharField(max_length=135)),
            ],
            options={
                'db_table': 'track_id',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserCredentials',
            fields=[
                ('user_id', models.CharField(serialize=False, primary_key=True, max_length=36)),
                ('password', models.CharField(max_length=75)),
            ],
            options={
                'db_table': 'user_credentials',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('user', models.ForeignKey(to='musicapp.UserCredentials', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=75)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=30)),
                ('location', models.CharField(blank=True, max_length=75)),
            ],
            options={
                'db_table': 'user_details',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserLibraries',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('listened_times', models.CharField(max_length=36)),
                ('song', models.ForeignKey(to='musicapp.MasterDb')),
                ('user', models.ForeignKey(to='musicapp.UserCredentials')),
            ],
            options={
                'db_table': 'user_libraries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserPlaylist',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('pl_id', models.CharField(unique=True, max_length=36)),
                ('pl_name', models.CharField(max_length=135)),
                ('user', models.ForeignKey(to='musicapp.UserCredentials')),
            ],
            options={
                'db_table': 'user_playlist',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='playlistentry',
            name='pl',
            field=models.ForeignKey(to='musicapp.UserPlaylist'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='playlistentry',
            name='song',
            field=models.ForeignKey(to='musicapp.MasterDb'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='masterdb',
            name='release_lbl',
            field=models.ForeignKey(to='musicapp.ReleaseLbl'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='masterdb',
            name='track',
            field=models.ForeignKey(to='musicapp.Track'),
            preserve_default=True,
        ),
    ]
