from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('jwt/create/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(),
         name='token_verify'),

    path('', include(router.urls)),

    # Вложенные ручные маршруты комментариев к постам
    path('posts/<int:post_id>/comments/',
         CommentViewSet.as_view({'get': 'list',
                                 'post': 'create'}),
         name='post-comments-list'),
    path('posts/<int:post_id>/comments/<int:pk>/',
         CommentViewSet.as_view({'get': 'retrieve',
                                 'put': 'update',
                                 'patch': 'partial_update',
                                 'delete': 'destroy'}),
         name='post-comments-detail'),
]
