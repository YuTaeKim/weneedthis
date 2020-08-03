from django.urls import path

from . import views

app_name='board'

urlpatterns = [
    path('', views.index, name='index'),
    path('board/about_site/', views.about_site, name='about_site'),
    path('board/signup/', views.signup, name='signup'),
    path('board/signup/username_check/', views.username_check, name='username_check'),
    path('board/signup_success/', views.signup_success, name='signup_success'),
    path('board/signup_process/', views.signup_process, name='signup_process'),
    path('board/signup_fail/<str:error>/', views.signup_fail, name='signup_fail'),
    path('board/signin/', views.signin, name='signin'),
    path('board/signin_process/', views.signin_process, name='signin_process'),
    path('board/signin_success/', views.signin_success, name='signin_success'),
    path('board/signin_need/', views.signin_need, name='signin_need'),
    path('board/signin_fail/', views.signin_fail, name='signin_fail'),
    path('board/idea_list/', views.idea_list, name='idea_list'),
    path('board/idea_list/add_comment', views.add_comment, name='add_comment'),
    path('board/idea_list/delete_comment', views.delete_comment, name='delete_comment'),
    path('board/idea_list/update_comment', views.update_comment, name='update_comment'),
    path('board/idea_list/likes_process/', views.likes_process, name='likes_process'),
    path('board/idea_new/', views.idea_new, name='idea_new'),
    path('board/idea_delete/<int:pk>', views.idea_delete, name='idea_delete'),
    path('board/idea_edit/<int:pk>/', views.idea_edit, name='idea_edit'),
    path('board/logout_process/', views.logout_process, name='logout_process'),
    path('board/logout_success/', views.logout_success, name='logout_success'),
    path('board/about_user/', views.about_user, name='about_user'),
    path('board/about_user/user_update/', views.user_update, name='user_update'),
    path('board/about_user/user_update_success/', views.user_update_success, name='user_update_success'),
    path('board/about_user/user_update_fail/<str:error>', views.user_update_fail, name='user_update_fail'),
    path('board/about_user/user_update_process/', views.user_update_process, name='user_update_process'),
    path('board/about_user/user_idea/', views.user_idea, name='user_idea'),
    path('board/about_user/user_likes/', views.user_likes, name='user_likes'),
    path('board/application/', views.application, name='application'),
    path('board/feedback/', views.feedback, name='feedback'),
    path('board/motivation/', views.motivation, name='motivation'),
]