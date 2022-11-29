from django.urls import path, include
from rest_framework import routers
from . import views


# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'post', PostViewSet)
# router.register(r'comment', CommentViewSet)

# urlpatterns = [
#     path('', include(router.urls))
# ]

urlpatterns = [
    path('post/', views.PostListAPIView.as_view(), name='post-list'),
    path('post/<int:pk>', views.PostRetrieveAPIView.as_view(), name='post-detail'),
    path('comment/', views.CommentCreateAPIView.as_view(), name="comment-list")
]
