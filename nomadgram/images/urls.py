from django.conf.urls import url
from . import views

app_name = 'images'
urlpatterns = [
    url(
        regex=r'^$',
        view=views.Image.as_view(),
        name='Image'
    ),
    url(
        regex=r'^(?P<image_id>\w+)/$',
        view=views.ImageDetail.as_view(),
        name='ImageDetail'
    ),
    url(
        regex=r'^(?P<image_id>\w+)/like/',
        view=views.LikeImage.as_view(),
        name='like_image'
    ),
    url(
        regex=r'^(?P<image_id>\w+)/unlike/',
        view=views.UnlikeImage.as_view(),
        name='like_image'
    ),
    url(
        regex=r'^(?P<image_id>\w+)/comments/(?P<comment_id>[0-9]+)/$',
        view=views.ModerateComment.as_view(),
        name='ModerateComment'
    ),
    url(
        regex=r'^(?P<image_id>\w+)/comments/',
        view=views.CommentOnImage.as_view(),
        name='comment_image'
    ),
    url(
        regex=r'^comments/(?P<comment_id>[0-9]+)/$',
        view=views.Comment.as_view(),
        name='comment'
    ),
    url(
        regex=r'^search/$',
        view=views.Search.as_view(),
        name='Search'
    )

]