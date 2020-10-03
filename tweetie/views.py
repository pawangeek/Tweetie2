import json, re, requests, time
from urllib.parse import urlparse
from datetime import datetime

from django.http import Http404
from django.urls import reverse
from django.http import JsonResponse
from django.db.models import Count
from django.shortcuts import render, redirect
from authlib.integrations.django_client import OAuth

from .models import User, Tweets
from .utils import sevenspan, getlinks

oauth = OAuth()
oauth.register(
    name='twitter',
    api_base_url='https://api.twitter.com/1.1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authenticate',
    fetch_token=lambda: session.get(token),
)

def home(request):
    newuser = request.session.get('user')

    if newuser:
        newuser, created = User.objects.get_or_create(handleid=newuser['id'], name=newuser['screen_name'])

    return render(request, 'tweetie/home.html', context={'user': newuser})


def login(request):
    redirect_uri = request.build_absolute_uri(reverse('auth'))
    return oauth.twitter.authorize_redirect(request, redirect_uri)


def auth(request):
    token = oauth.twitter.authorize_access_token(request)
    url = 'https://api.twitter.com/1.1/account/verify_credentials.json'

    resp = oauth.twitter.get(url, params={'skip_status': True}, token=token)
    user = resp.json()

    request.session['token'] = token
    request.session['user'] = user

    return redirect('/')

def analysis(request):

    try:
        user = request.session['user'] 
    except:
        raise Http404("User not logged in")
    
    maxtweet = Tweets.objects.filter(handle=user['id']).\
                values('author').\
                annotate(total=Count('id')).\
                order_by('-total')[0]

    maxlink = Tweets.objects.filter(handle=user['id']).\
                values('website').\
                annotate(total=Count('id')).\
                order_by('-total')
    
    return render(request, 'tweetie/analyze.html', context={'maxtweet': maxtweet, 'maxlink':maxlink})


def list_tweets(request):

    url = 'statuses/home_timeline.json'
    params = {'include_rts': 0, 'count': 200, 'tweet_mode':'extended'}

    prev_id = request.GET.get('prev')
    if prev_id: params['max_id'] = prev_id

    try:
        token = request.session['token']
        resp = oauth.twitter.get(url, params=params, token = token)
    except:
        raise Http404("YOU should login")
    
    handleid = request.session['user']['id']

    tweets = resp.json()
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    
    for i in range(len(tweets)):
        mytext = tweets[i]['full_text']
        url = re.findall(regex, mytext)

        currdate = tweets[i]['created_at']
        currobj = datetime.strptime(currdate,'%a %b %d %H:%M:%S +0000 %Y')

        if url and currobj > sevenspan() :

            if Tweets.objects.filter(tweetid=tweets[i]['id']).exists() is False:
                finalurl = tweets[i]['entities']['urls']

                if finalurl:
                    finaldest, domain = getlinks(finalurl[0]['expanded_url'])
                    Tweets(text = tweets[i]['full_text'], tweetid = tweets[i]['id'], \
                            author = tweets[i]['user']['screen_name'], link = finaldest, \
                            website = domain, created_at = currobj, handle = handleid).save()

        elif currobj > sevenspan():
            continue
        else:
            break
    
    tweeties = Tweets.objects.filter(handle=handleid).order_by('-id')
    return render(request, 'tweetie/tweet.html', context={'tweets': tweeties, 'last_tweet':tweets[-1]})

def about(request):
    return render(request, 'tweetie/about.html')

def logout(request):
    request.session.pop('user', None)
    request.session.pop('token', None)

    return redirect('/')
