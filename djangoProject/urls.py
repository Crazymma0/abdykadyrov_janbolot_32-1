"""
URL configuration for Blog32 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from apps.posts import views as posts_views
from djangoProject.settings import MEDIA_URL, MEDIA_ROOT

from users import views as users_view


urlpatterns = [
    path('admin/', admin.site.urls),

    # posts
    path('', posts_views.main_view),
    path('posts/', posts_views.posts_view),
    path('posts/<int:id>/', posts_views.post_detail_view),
    path('posts/create/', posts_views.post_create_view),

    # hashtags
    path('hashtags/', posts_views.hashtags_view),
    #users
    path('users/register/', users_view.register_view)

]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)