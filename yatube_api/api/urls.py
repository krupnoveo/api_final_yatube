from django.urls import path, include
from rest_framework.routers import SimpleRouter
from api import views


router = SimpleRouter()
router.register(
    r'posts',
    views.PostViewSet,
)
router.register(
    r'groups',
    views.GroupViewSet
)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    views.CommentViewSet,
)
router.register(
    'follow',
    views.FollowViewSet,
)
urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
