from snippets.views import SnippetViewSet, UserViewSet
from rest_framework import renderers

site_list = SiteViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
site_detail = SiteViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})


urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),
    url(r'^sites/$', site_list, name='site-list'),
    url(r'^sites/(?P<pk>[0-9]+)/$', site_detail, name='site-detail'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
])