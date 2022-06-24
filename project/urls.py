from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from src.blog import views

router = SimpleRouter()
router.register(r'post', views.PostViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'rate', views.RateViewSet)
router.register(r'comment', views.CommentViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += router.urls
