import os
from flask import Flask

from services import bitbucket
from services import deviantart
from services import digg
from services import disqus
from services import dropbox
from services import etsy
from services import facebook
from services import fitbit
from services import flickr
from services import github
from services import instagram
from services import twitter

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

def init_services(*services):
    service_list = []

    for service in services:
        alias = service.alias.upper()
        key = os.environ.get('%s_KEY' % alias, '').decode('utf8')
        secret = os.environ.get('%s_SECRET' % alias, '').decode('utf8')

        if key and secret: # Only initialize if all the pieces are in place
            service_list.append(service(key, secret))

    return service_list

services = init_services(bitbucket.Bitbucket,
                         deviantart.DeviantArt,
                         digg.Digg,
                         disqus.Disqus,
                         dropbox.Dropbox,
                         etsy.Etsy,
                         facebook.Facebook,
                         fitbit.FitBit,
                         flickr.Flickr,
                         github.GitHub,
                         instagram.Instagram,
                         twitter.Twitter)
