from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views 



urlpatterns=[
    path('register/', views.register_view, name='register_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('account_confirm/<slug:uidb64>/<slug:token>/',views.activate,name="account_confirm_email"),#### route de confirmation du mail
    path('login/', views.login_view, name='login_view'),
]