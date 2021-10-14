from django.contrib import admin
from django.urls import path, include

app_name = 'main'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls', namespace='posts')),
    path('account/', include('account.urls', namespace='account')),
]
