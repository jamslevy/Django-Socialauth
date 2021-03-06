from django.conf.urls.defaults import *
from openid_consumer.views import begin, complete, signout
from django.views.generic.simple import direct_to_template

from django.conf import settings

post_login_url = r'^%s$'%settings.LOGIN_REDIRECT_URL[1:]

#Login Views
urlpatterns = patterns('socialauth.views',
    url(r'^xd_receiver.htm$', direct_to_template, {'template':'socialauth/xd_receiver.htm'}, name='socialauth_xd_receiver'),
    url(r'^facebook_login/done/', 'facebook_login_done', name='socialauth_facebook_login_done'),
    url(r'^login/$', 'login_page', name='socialauth_login_page'),
    url(post_login_url, 'signin_complete', name='socialauth_signin_complete'),
    url(r'^twitter_login/$', 'twitter_login', name='socialauth_twitter_login'),
    url(r'^twitter_login/done/$', 'twitter_login_done', name='socialauth_twitter_login_done'),
    url(r'^yahoo_login/$', 'yahoo_login', name='socialauth_yahoo_login'),
    url(r'^yahoo_login/complete/$', complete, name='socialauth_yahoo_complete'),
    url(r'^gmail_login/$', 'gmail_login', name='socialauth_google_login'),
    url(r'^gmail_login/complete/$', complete, name='socialauth_google_complete'),
    url(r'^openid/$', 'openid_login', name='socialauth_openid_login'),
    url(r'^openid/complete/$', complete, name='socialauth_openid_complete'),
    url(r'^openid/signout/$', signout, name='openid_signout'),
    url(r'^openid/done/$', 'openid_done', name='openid_openid_done'),
)

#Other views.
urlpatterns += patterns('socialauth.views',
    url(r'^logout/$', 'social_logout',  name='socialauth_social_logout'),
) 