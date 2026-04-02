from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('hotelproperties/', views.hotelproperty_list, name='hotelproperty_list'),
    path('hotelproperties/create/', views.hotelproperty_create, name='hotelproperty_create'),
    path('hotelproperties/<int:pk>/edit/', views.hotelproperty_edit, name='hotelproperty_edit'),
    path('hotelproperties/<int:pk>/delete/', views.hotelproperty_delete, name='hotelproperty_delete'),
    path('roombookings/', views.roombooking_list, name='roombooking_list'),
    path('roombookings/create/', views.roombooking_create, name='roombooking_create'),
    path('roombookings/<int:pk>/edit/', views.roombooking_edit, name='roombooking_edit'),
    path('roombookings/<int:pk>/delete/', views.roombooking_delete, name='roombooking_delete'),
    path('hotelguests/', views.hotelguest_list, name='hotelguest_list'),
    path('hotelguests/create/', views.hotelguest_create, name='hotelguest_create'),
    path('hotelguests/<int:pk>/edit/', views.hotelguest_edit, name='hotelguest_edit'),
    path('hotelguests/<int:pk>/delete/', views.hotelguest_delete, name='hotelguest_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
