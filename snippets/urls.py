from django.urls import include, path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

appname = 'snippets'

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]


urlpatterns = format_suffix_patterns(urlpatterns)