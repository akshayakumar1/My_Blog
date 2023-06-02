from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


## localhost:8000/myapp/home
urlpatterns = [
    path('',views.main),
    path("home", views.home, name="home"),
    path('regeister',views.regeister,name='regeister'),
    path('login',views.user_login,name='login'),
    path('logout',views.user_logout,name='logout'),
    path('blog_post',views.blog_post,name='blog_post'),
    path('all_posts',views.display_all_post,name='all_posts'),
    path('post_details/<int:id>',views.display_post,name='post_details'),
    path('edit_post/<int:id>',views.edit_post,name='edit_post'),
    path('delete_post/<int:id>',views.delete_post,name='delete_post'),
    path('contact',views.contact,name='contact'),
    path('change_password',views.change_password,name="change_password"),
    path('change_username',views.change_username,name='change_username'),

    path('password_reset',auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),name='password_reset'),
    path('password_reset_done',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),


]


"""
forget password default views.. inside auth_views

accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']

"""
