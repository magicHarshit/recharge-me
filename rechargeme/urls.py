from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'rechargeproviders.views.home', name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login',
            {'template_name':'login.html'}),
    url(r'^logout/$','django.contrib.auth.views.logout',
            {'extra_context':{'message':'You have been logged out'},
            'template_name':'login.html'}),
    url(r'^signup', 'rechargeme.views.signup', name='signup'),
    url(r'^recharge/(?P<ph_id>\d+)/$', 'transactions.views.recharge'),
    url(r'^profile/mynumbers/$', 'rechargeme.views.showmynumbers'),
    url(r'^profile/addmoney/$', 'rechargeme.views.addmoney'),
    url(r'^profile/$', 'rechargeme.views.profile'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}))
