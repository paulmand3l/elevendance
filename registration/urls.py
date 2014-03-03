from django.conf.urls import patterns, include, url

urlpatterns = patterns('checkin.views',
    url(r'^checkin/$', 'checkin', name="checkin-checkin"),
)
