from django.conf.urls import patterns, include, url

urlpatterns = patterns('payroll.views',
    url(r'^closeout$', 'close_out', name="payroll-closeout"),
)
