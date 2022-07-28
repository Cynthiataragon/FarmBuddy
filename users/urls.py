# api first django app
from views import register


from django.urls import path, include

urlpatterns = [
    path('register/', views.register_request, name='register'),
    path('home/', home, name='hpme'),
    path('login/', auth_views.LoginView.as_view(template_name=' users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
   
]