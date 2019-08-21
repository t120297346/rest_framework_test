from django.conf.urls import url, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^snippets/(?P<pk>[0-9]+)/', views.SnippetDetail.as_view()),#django < 2.0 需用這個形式, > 2.0 可用<int:pk>取代 (?P<pk>[0-9]+)
    url(r'^snippets/', views.SnippetList.as_view()),
    url(r'^users/', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/', views.UserDetail.as_view()),    
]
urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')), #api-auth/login/
]
 
