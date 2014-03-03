from django.conf.urls import patterns, url

urlpatterns = patterns('django.contrib.staticfiles.views',
    url(r'^$', 'serve', { 'path': 'index.html'}, name="base-index"),
)
