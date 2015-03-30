from django.http import HttpResponse
from .models import MasterDb, UserPlaylist
from django.db import connection
import django.contrib.auth
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import redirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
#main page
def main(request):
    """Main listing."""
    if request.user.is_authenticated():
        cur=connection.cursor()
        print("logged in")
        print(request.user.username)
        query='Select id from auth_user where username="'+str(request.user.username)+'";'
        cur.execute(query)
        posts=cur.fetchone()
        user_id=posts[0]
        query='Select pl_id,pl_name from user_playlist where user_id="'+str(user_id)+'";'
        cur.execute(query)
        posts=cur.fetchone()
        pl_id=posts[0]
        query='Select * from master_db where song_id not in (select distinct song_id from playlist_entry where pl_id="'+str(pl_id)+'");'
        cur.execute(query)
        posts=cur.fetchall()
        x = cur.description
        resultsList = []
        for r in posts:
                i = 0
                d = {}
                while i < len(x):
                    d[x[i][0]] = str(r[i])
                    i = i+1
                resultsList.append(d)
        paginator = Paginator(resultsList, 4)
        try: page = int(request.GET.get("page", '1'))
        except ValueError: page = 1

        try:
            resultsList = paginator.page(page)
        except (InvalidPage, EmptyPage):
            resultsList = paginator.page(paginator.num_pages)
        return render_to_response("Addmore.html", dict(posts=resultsList),context_instance=RequestContext(request))

    else:
        posts = MasterDb.objects.all()
        print(type(posts))
        paginator = Paginator(posts, 4)
        try: page = int(request.GET.get("page", '1'))
        except ValueError: page = 1

        try:
            posts = paginator.page(page)
        except (InvalidPage, EmptyPage):
            posts = paginator.page(paginator.num_pages)
        return render_to_response("Addmore.html", dict(posts=posts),context_instance=RequestContext(request))
#get top tracks
def getTopTrack(request):
    """Main listing."""
    if request.user.is_authenticated():
        cur=connection.cursor()
        print("logged in")
        print(request.user.username)
        query='Select id from auth_user where username="'+str(request.user.username)+'";'
        cur.execute(query)
        posts=cur.fetchone()
        user_id=posts[0]
        query='Select pl_id,pl_name from user_playlist where user_id="'+str(user_id)+'";'
        cur.execute(query)
        posts=cur.fetchone()
        pl_id=posts[0]
        query='Select * from master_db where song_id not in (select distinct song_id from playlist_entry where pl_id="'+str(pl_id)+'") order by download_times desc limit 10;'
        cur.execute(query)
        posts=cur.fetchall()
        x = cur.description
        resultsList = []
        for r in posts:
                i = 0
                d = {}
                while i < len(x):
                    d[x[i][0]] = str(r[i])
                    i = i+1
                resultsList.append(d)
        paginator = Paginator(resultsList, 4)
        try: page = int(request.GET.get("page", '1'))
        except ValueError: page = 1

        try:
            resultsList = paginator.page(page)
        except (InvalidPage, EmptyPage):
            resultsList = paginator.page(paginator.num_pages)
        return render_to_response("Addmore.html", dict(posts=resultsList),context_instance=RequestContext(request))

    else:
        cur=connection.cursor()
        query='Select * from master_db order by download_times desc limit 10;'
        cur.execute(query)
        posts=cur.fetchall()
        x = cur.description
        resultsList = []
        for r in posts:
                i = 0
                d = {}
                while i < len(x):
                    d[x[i][0]] = str(r[i])
                    i = i+1
                resultsList.append(d)
        paginator = Paginator(resultsList, 4)
        try: page = int(request.GET.get("page", '1'))
        except ValueError: page = 1

        try:
            resultsList = paginator.page(page)
        except (InvalidPage, EmptyPage):
            resultsList = paginator.page(paginator.num_pages)
        return render_to_response("Addmore.html", dict(posts=resultsList),context_instance=RequestContext(request))
@login_required
def getUserPlaylist(request):
    """Main listing."""
    cur=connection.cursor()
    if request.user.is_authenticated():
        print("logged in")
        print(request.user.username)
    query='Select id from auth_user where username="'+str(request.user.username)+'";'
    cur.execute(query)
    posts=cur.fetchone()
    user_id=posts[0]
    query='Select pl_id,pl_name from user_playlist where user_id="'+str(user_id)+'";'
    cur.execute(query)
    posts=cur.fetchone()
    pl_id=posts[0]
    query='Select * from master_db where song_id in (select distinct song_id from playlist_entry where pl_id="'+str(pl_id)+'");'
    cur.execute(query)
    posts=cur.fetchall()
    x = cur.description
    resultsList = []
    for r in posts:
            i = 0
            d = {}
            while i < len(x):
                d[x[i][0]] = str(r[i])
                i = i+1
            resultsList.append(d)
    paginator = Paginator(resultsList, 2)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        resultsList = paginator.page(page)
    except (InvalidPage, EmptyPage):
        resultsList = paginator.page(paginator.num_pages)
    print(dict(posts=resultsList))
    return render_to_response("showPlaylist.html", dict(posts=resultsList),context_instance=RequestContext(request))

@login_required
def addToPlaylist(request):
    print(request)
    id_to_add=request.GET['id']
    cur=connection.cursor()
    if request.user.is_authenticated():
        print("logged in")
        print(request.user.username)
    query='Select id from auth_user where username="'+str(request.user.username)+'";'
    cur.execute(query)
    posts=cur.fetchone()
    user_id=posts[0]
    query='Select pl_id,pl_name from user_playlist where user_id="'+str(user_id)+'";'
    cur.execute(query)
    posts=cur.fetchone()
    pl_id=posts[0]
    query='Select * from playlist_entry where song_id ="'+id_to_add+'" and pl_id="'+pl_id+'"'
    cur.execute(query)
    posts=cur.fetchall()
    if len(posts)>0:
        return HttpResponse("Song already exist in playlist")
    else:
        query='insert into `music`.`playlist_entry` (`pl_id`,`song_id`) values ("'+pl_id+'","'+id_to_add+'")'
        cur.execute(query)
        return redirect("/userPlaylists")


@login_required
def removeFromPlaylist(request):
    id_to_add=request.GET['id']
    cur=connection.cursor()
    if request.user.is_authenticated():
        print("logged in")
        print(request.user.username)
    query='Select id from auth_user where username="'+str(request.user.username)+'";'
    cur.execute(query)
    posts=cur.fetchone()
    user_id=posts[0]
    query='Select pl_id,pl_name from user_playlist where user_id="'+str(user_id)+'";'
    cur.execute(query)
    posts=cur.fetchone()
    pl_id=posts[0]
    query='delete from playlist_entry where song_id ="'+id_to_add+'" and pl_id="'+pl_id+'"'
    cur.execute(query)
    return redirect("/userPlaylists")