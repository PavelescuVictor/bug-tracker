"""ISS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import path
from . import views
from .views import (
    BugListView,
    BugDetailView,
    BugCreateView,
    BugUpdateView,
    BugDeleteView,
)

urlpatterns = [
    path('', BugListView.as_view(), name='bugtracker-home'),
    path('home/', BugListView.as_view(), name='bugtracker-home'),
    path('about/', views.about, name='bugtracker-about'),
    path('registerbug/', BugCreateView.as_view(), name='bugtracker-register-bug'),
    path('buglist/', BugListView.as_view(), name='bugtracker-list-bug'),
    path('buglist/<int:pk>',  BugDetailView.as_view(), name='bug-detail'),
    path('buglist/<int:pk>/update/', BugUpdateView.as_view(), name='bug-update'),
    path('buglist/<int:pk>/delete/', BugDeleteView.as_view(), name='bug-delete')
]
