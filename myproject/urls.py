"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('change_done/',views.change_done, name='change_done'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='todo/password_reset.html',success_url = reverse_lazy('password_reset_done')), name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='todo/password_reset_done.html'),name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='todo/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='todo/password_reset_complete.html'), name='password_reset_complete'),

    # Todos
    path('', views.home, name='home'),
    path('create/', views.createtodo, name='createtodo'),
    path('current/', views.currenttodos, name='currenttodos'),
    path('completed/', views.completedtodos, name='completedtodos'),
    path('todo/<int:todo_pk>', views.viewtodo, name='viewtodo'),
    path('todo/<int:todo_pk>/complete', views.completetodo, name='completetodo'),
    path('todo/<int:todo_pk>/delete', views.deletetodo, name='deletetodo'),
]
