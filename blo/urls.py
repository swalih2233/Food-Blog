from django.urls import path

from blo import views

app_name = "blo"
urlpatterns = [
    path("",views.index, name="index"),
    path("category/<int:id>/",views.category, name="category"),

    path("account/",views.account, name="account"),
    path("blog/<int:id>/", views.blog, name="blog"),
    path("blog/delete/<int:id>/", views.blog_del, name="blog_del"),
    path("blog/edit/<int:id>/", views.blog_edit, name="blog_edit"),

    path("create/", views.create, name="create"),
    path("login/", views.login, name="login"),
    path("logout/",views.logout, name="logout"),
    path("register/", views.register, name="register")



]