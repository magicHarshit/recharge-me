from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin

from Information.api import PhoneNumberList, PhoneNumberDetail, OperatorList, UserAccountDetail, UserAccountList
from Information.views import *
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'Information.views.home', name='home'),

    url(r'^api/numbers/$', PhoneNumberList.as_view()),
    #fetch article whose id== pk
    url(r'^api/number/(?P<pk>[0-9]+)/$', PhoneNumberDetail.as_view()),

    url(r'^api/operators/$', OperatorList.as_view()),

    url(r'^api/account/$', UserAccountList.as_view()),

    url(r'^account/update/$', update_balance),

    url(r'^api/account/(?P<pk>[0-9]+)/$', UserAccountDetail.as_view()),

    url(r'^login/$', 'django.contrib.auth.views.login',
            {'template_name':'login.html'}),

    url(r'^logout/$','django.contrib.auth.views.logout',
            {'extra_context':{'message':'You have been logged out'},
            'template_name':'login.html'})
)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}))
