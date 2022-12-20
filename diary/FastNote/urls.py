from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('auth/login/', views.CustomLoginView.as_view(), name='login'),
    path('', views.AllUserNotes.as_view(), name='notes'),
    path('auth/logout/', LogoutView.as_view(next_page='login'), name='logout'),
]