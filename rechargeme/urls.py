from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'rechargeapi.views.home', name='home'),
    url(r'^addphones/$', 'operators.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
)
