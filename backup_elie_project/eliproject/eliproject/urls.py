

from django.contrib import admin
from django.urls import path
from home import views
# from django.contrib.auth import views as auth_views
from django.conf.urls import url,include

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('index/',views.index, name='index'),
    # path('',views.password_users, name='password'),
    path('data.csv/',views.csv_download, name='sign in'),
    path('instagram/',views.show_following, name='following'),
    path('insert_a/',views.insert_a, name='a'),
    path('insert_b/',views.insert_group_b, name='b'),
    path('follow/',views.follow_added_A, name='follow'),
    path('delete/',views.delete_user_a, name='a'),
    path('deletes/',views.delete_user_b, name='b'),
    path('follows/',views.follow_added_B, name='follows'),
    path('feed/',views.feed_page, name="feed page"),
    # path('wrong/',views.rong, name='Rong'),
    path('logout/',views.logout_request, name=' Logout'),
    path('delete_user/',views.dell_search, name='dell'),
    path('delete_b/',views.dell_search_b, name='dell_b'),

]


