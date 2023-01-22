from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url, include
from .import views
from .import views
from .views import (PostsView, PostDetailView, RecentTags,PopularTags,PostsFilterByTagView)
from django.conf import settings
from django.conf.urls.static import static


# from rest_framework import routers
# router = routers.DefaultRouter()

# router.register(r'blog/posts', PostsViewSet)

app_name="blogs_api"
urlpatterns = [
    path('', PostsView.as_view(), name='posts-list'),
    path('/post-detail/<int:id>/', PostDetailView, name='post-detail'),
    path('/recent-tags', RecentTags, name='recent-tags'),
    path('/popular-tags', PopularTags, name='popular-tags'),
    path('/post-filter-tag/<int:id>/', PostsFilterByTagView, name='posts-filter-tag'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
