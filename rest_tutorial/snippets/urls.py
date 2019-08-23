from django.conf.urls import url, include
from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter


snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    url(r'^$', api_root),
    url(r'^snippets/', snippet_list, name = 'snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/', snippet_detail, name = 'snippet-detail'),#django < 2.0 需用這個形式, > 2.0 可用<int:pk>取代 (?P<pk>[0-9]+)
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/', snippet_highlight, name = 'snippet-highlight'),
    url(r'^users/', user_list, name = 'user-list'),
    url(r'^users/(?P<pk>[0-9]+)/', user_detail, name = 'user-detail'),    
]
urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')), #api-auth/login/
    #url('', include(router.urls))
]

 # Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'users', UserViewSet)