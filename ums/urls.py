from ums.views import admin_dashboard, close_ticket
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name="homepage"),
    path('logout', views.log_out, name='logout'),
    path('login', views.sign_in, name="sign_in"),
    path('request', views.request_new_user, name="request_new_user"),


    path('usr/profile', views.user_profile, name='user_profile'),
    path('usr/profile/edit', views.edit_profile, name='edit_profile'),
    path('usr/support', views.user_support, name='user_support'),
    path('usr/support/del/<int:pk>',
         views.close_ticket_user, name="close_ticket_user"),


    path('admin', views.admin_dashboard, name='admin_dashboard'),
    path('admin/new-usr', views.new_user, name="new_user"),
    path('admin/usr/del/<int:pk>', views.delete_user, name='delete_user'),
    path('admin/usr/edit/<int:pk>', views.edit_user, name='edit_user'),
    path('admin/mg-usr', views.all_users, name='all_users'),
    path('admin/mg-usr/inactive', views.inactive_users, name='inactive_users'),
    path('admin/mg-usr/active', views.active_users, name='active_users'),
    path('admin/mg-usr/search', views.search_user, name='search_users'),


    path('admin/mg-usr/user-request', views.view_request_users, name='view_request_users'),


    path('admin/usr/block/<int:pk>', views.toggle_block, name='toggle_block'),
    path('admin/usr/reset/<int:pk>', views.reset_password, name='reset_password'),
    path('admin/profile', views.admin_profile, name='admin_profile'),
    path('admin/usr/make-admin/<int:pk>',
         views.toggle_admin_role, name='toggle_admin_role'),
    path('admin/mg-tickets', views.support_tickets, name='support_tickets'),
    path('admin/mg-tickets/del/<int:pk>',
         views.close_ticket, name="close_ticket"),
    # path('admin/profile/edit',views.edit_admin,name='edit_admin'),
]
