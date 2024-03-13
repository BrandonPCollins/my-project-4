from django.urls import path
#from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView, PasswordsChangeView, AddCommentView, EditComment
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail' ),
    path( 'add_post/', AddPostView.as_view(), name='add_post'),
    path( 'add_category/', AddCategoryView.as_view(), name='add_category'),
    path( 'article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post' ),
    path( 'article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post' ),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list', CategoryListView, name='category-list'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('comment/<int:comment_id>/edit/', EditComment, name='edit_comment'),

    path('<int:uid>/password/', PasswordsChangeView.as_view(template_name='change-password.html')),
    path('password_success', views.password_success, name="password_success"),

]
