from django.urls import path

from . import views

app_name='board'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signup/username_check/', views.username_check, name='username_check'),
    path('signup_success/', views.signup_success, name='signup_success'),
    path('signup_process/', views.signup_process, name='signup_process'),
    path('signup_fail/<str:error>/', views.signup_fail, name='signup_fail'),
    path('signin/', views.signin, name='signin'),
    path('signin_process/', views.signin_process, name='signin_process'),
    path('signin_success/', views.signin_success, name='signin_success'),
    path('signin_need/', views.signin_need, name='signin_need'),
    path('signin_fail/', views.signin_fail, name='signin_fail'),
    path('idea_list/', views.idea_list, name='idea_list'),
    path('idea_list/likes_process/', views.likes_process, name='likes_process'),
    path('idea_new/', views.idea_new, name='idea_new'),
    path('idea_delete/<int:pk>', views.idea_delete, name='idea_delete'),
    path('idea_edit/<int:pk>/', views.idea_edit, name='idea_edit'),
    path('logout_process/', views.logout_process, name='logout_process'),
    path('logout_success/', views.logout_success, name='logout_success'),
    path('about_user/', views.about_user, name='about_user'),
    path('about_user/user_update/', views.user_update, name='user_update'),
    path('about_user/user_update_success/', views.user_update_success, name='user_update_success'),
    path('about_user/user_update_fail/<str:error>', views.user_update_fail, name='user_update_fail'),
    path('about_user/user_update_process/', views.user_update_process, name='user_update_process'),
    path('about_user/user_idea/', views.user_idea, name='user_idea'),
    path('about_user/user_likes/', views.user_likes, name='user_likes'),
    path('application/', views.application, name='application'),
    path('feedback/', views.feedback, name='feedback'),
]