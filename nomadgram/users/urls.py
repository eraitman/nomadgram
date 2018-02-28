from django.conf.urls import url

from . import views

app_name = 'users'
urlpatterns = [
    url(
        regex=r'^explore/$',
        view=views.ExploreUsers.as_view(),
        name='ExploreUsers  '
    ),
    url(
        regex=r'^(?P<user_id>[0-9]+)/follow/$',
        view=views.FollowUser.as_view(),
        name='follow'
    ),
    url(
        regex=r'^(?P<user_id>[0-9]+)/unfollow/$',
        view=views.UnfollowUsers.as_view(),
        name='unfollow'
    ),
     url(
        regex=r'^search/$',
        view=views.Search.as_view(),
        name='User Search'
    ),
    url(
        regex=r'^(?P<username>\w+)/$',
        view=views.UserProfile.as_view(),
        name='UserProfile'
    ),
     url(
        regex=r'^(?P<username>\w+)/followers/$',
        view=views.UserFollowers.as_view(),
        name='view followers'
    ),
    url(
        regex=r'^(?P<username>\w+)/followings/$',
        view=views.UserFollowings.as_view(),
        name='view UserFollowings'
    ),
    url(
        regex=r'^(?P<username>\w+)/password/$',
        view=views.ChangePassword.as_view(),
        name='ChangePassword'
    ),
    url(r'^login/facebook/$', views.FacebookLogin.as_view(), name='fb_login')
    
   
]
