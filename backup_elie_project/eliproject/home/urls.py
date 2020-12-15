

from django.contrib import admin
from django.urls import path,include
from home import views
# app_name = 'home'
from django.conf.urls import url

urlpatterns = [

    # path('admin/', admin.site.urls),
    # path('', include('home.urls')),
    path('index/',views.index, name='index'),
    path('',views.user_login, name='user_login'),
    # url(r'^user_login/$',views.user_login,name='user_login'),
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
    path('delete_user/',views.dell_search, ),
    path('delete_b/',views.dell_search_b, ),

]


