# -*- coding: utf-8 -*-
from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns, include, url

admin.autodiscover()

urlpatterns = patterns('',
    # admin
    url(r'^admin/', include(admin.site.urls)),
    # projects
    url(r'^$',
        'libreqda.views.home',
        name='home'),
    url(r'^project/$',
        'libreqda.views.browse_projects',
        name='browse_projects'),
    url(r'^project/new/$',
        'libreqda.views.new_project',
        name='new_project'),
    url(r'^project/(?P<pid>\d+)/delete/$',
        'libreqda.views.delete_project',
        name='delete_project'),
    url(r'^project/(?P<pid>\d+)/copy/$',
        'libreqda.views.copy_project',
        name='copy_project'),
    url(r'^project/(?P<pid>\d+)/user/add/$',
        'libreqda.views.add_user_to_project',
        name='add_user_to_project'),
    url(r'^project/(?P<pid>\d+)/user/(?P<uid>\d+)/remove/$',
        'libreqda.views.remove_user_from_project',
        name='remove_user_from_project'),
    # documents
    url(r'^project/(?P<pid>\d+)/document/(?P<did>\d+)/$',
        'libreqda.views.view_document',
        name='view_document'),
    url(r'^project/(?P<pid>\d+)/document/add/$',
        'libreqda.views.upload_document',
        name='upload_document'),
    url(r'^project/(?P<pid>\d+)/document/(?P<did>\d+)/delete/$',
        'libreqda.views.delete_document',
        name='delete_document'),
    #codes
    url(r'^project/(?P<pid>\d+)/code/$',
        'libreqda.views.browse_codes',
        name='browse_codes'),
    url(r'^project/(?P<pid>\d+)/code/new/$',
        'libreqda.views.new_code',
        name='new_code'),
    url(r'^project/(?P<pid>\d+)/code/(?P<cid>\d+)/delete/$',
        'libreqda.views.delete_code',
        name='delete_code'),
    #annotations
    url(r'^project/(?P<pid>\d+)/annotation/$',
        'libreqda.views.browse_annotations',
        name='browse_annotations'),
    url(r'^project/(?P<pid>\d+)/annotation/new/$',
        'libreqda.views.new_annotation',
        name='new_annotation'),
    url(r'^project/(?P<pid>\d+)/annotation/(?P<aid>\d+)/delete/$',
        'libreqda.views.delete_annotation',
        name='delete_annotation'),
    url(r'^project/(?P<pid>\d+)/annotation/(?P<aid>\d+)/code/add/$',
        'libreqda.views.add_code_to_annotation',
        name='add_code_to_annotation'),
    url(r'^project/(?P<pid>\d+)/annotation/(?P<aid>\d+)/code/remove/(?P<cid>\d+)/$',
        'libreqda.views.remove_code_from_annotation',
        name='remove_code_from_annotation'),
    #citations
    url(r'^project/(?P<pid>\d+)/citation/(?P<cid>.+)/assign/$',
        'libreqda.views.add_code_to_citation',
        name='add_code_to_citation'),
    # accounts
    url(r'^accounts/login/$',
        'django.contrib.auth.views.login',
        name='login'),
    url(r'^accounts/logout/$',
        'django.contrib.auth.views.logout',
        name='logout',
        kwargs={'next_page': '/accounts/login'}),
    #queries
    url(r'^project/(?P<pid>\d+)/query/$',
        'libreqda.views.browse_queries',
        name='browse_queries'),
    url(r'^project/(?P<pid>\d+)/query/boolean/new/$',
        'libreqda.views.new_boolean_query',
        name='new_boolean_query'),
    url(r'^project/(?P<pid>\d+)/query/boolean/delete/(?P<qid>\d+)/$',
        'libreqda.views.delete_boolean_query',
        name='delete_boolean_query'),
    url(r'^project/(?P<pid>\d+)/query/set/new/$',
        'libreqda.views.new_set_query',
        name='new_set_query'),
    url(r'^project/(?P<pid>\d+)/query/set/delete/(?P<qid>\d+)/$',
        'libreqda.views.delete_set_query',
        name='delete_set_query'),
    url(r'^project/(?P<pid>\d+)/query/proximity/new/$',
        'libreqda.views.new_proximity_query',
        name='new_proximity_query'),
    url(r'^project/(?P<pid>\d+)/query/proximity/delete/(?P<qid>\d+)/$',
        'libreqda.views.delete_proximity_query',
        name='delete_proximity_query'),
    url(r'^project/(?P<pid>\d+)/query/boolean/(?P<qid>\d+)/$',
        'libreqda.views.do_boolean_query',
        name='do_boolean_query'),
    url(r'^project/(?P<pid>\d+)/query/set/(?P<qid>\d+)/$',
        'libreqda.views.do_set_query',
        name='do_set_query'),
    url(r'^project/(?P<pid>\d+)/query/proximity/(?P<qid>\d+)/$',
        'libreqda.views.do_proximity_query',
        name='do_proximity_query'),
    # annotator
    url(r'^project/(?P<pid>\d+)/document/(?P<did>\d+)/annotations/create/$',
        'libreqda.annotations_views.create',
        name='annotations_create'),
    url(r'^project/(?P<pid>\d+)/document/(?P<did>\d+)/annotations/read/$',
        'libreqda.annotations_views.read',
        name='annotations_read'),
    url(r'^project/(?P<pid>\d+)/document/(?P<did>\d+)/annotations/read/(?P<aid>\d+)$',
        'libreqda.annotations_views.read',
        name='annotations_read'),
    url(r'^project/(?P<pid>\d+)/document/(?P<did>\d+)/annotations/destroy/$',
        'libreqda.annotations_views.destroy',
        name='annotations_destroy'),
    url(r'^project/(?P<pid>\d+)/document/(?P<did>\d+)/annotations/destroy/(?P<aid>\d+)$',
        'libreqda.annotations_views.destroy',
        name='annotations_destroy'),
    url(r'^project/(?P<pid>\d+)/document/(?P<did>\d+)/annotations/update/$',
        'libreqda.annotations_views.update',
        name='annotations_update'),
    url(r'^project/(?P<pid>\d+)/document/(?P<did>\d+)/annotations/update/(?P<aid>\d+)$',
        'libreqda.annotations_views.update',
        name='annotations_update'),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )
