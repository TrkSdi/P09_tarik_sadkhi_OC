"""LIT_Review URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from login.views import signup, logout_user
from django.contrib.auth import views as auth_views
from website.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name="login/signin.html",
                                                 redirect_authenticated_user=True), name="login"),
    path('logout/', logout_user, name="logout"),
    path('signup/', signup, name='signup'),
    path('feed/', feed, name='feed'),
    path('follow-page/', follow, name="follow-page"),
    path('follow-page/unfollow/', unfollow, name="follow-page-unfollow"),
    path('ticket/', ticket, name='ticket'),
    path('ticket/edit/<int:ticket_id>/', edit_ticket, name='ticket-edit'),
    path('ticket/delete/<int:ticket_id>/', delete_ticket, name="ticket-delete"),
    path('review/', review, name="review"),
    path('review/edit/<int:review_id>/', edit_review, name='review-edit'),
    path('review/delete/<int:review_id>/', delete_review, name="review-delete"),
    path('posts/', posts, name='posts'),
    path('feed/ticket/<int:ticket_id>/', ticket_review, name="ticket-review"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)