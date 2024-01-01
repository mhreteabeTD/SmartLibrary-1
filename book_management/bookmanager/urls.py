from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name="home"),
    path('list/',views.book_list,name='book_list'),
    path('add/',views.add_book,name='add_book'),
    path('edit/<int:pk>/', views.edit_book,name="edit_book"),
    path('configure-library/',views.configure_library,name="configure_library"),
    path('add_library_level/',views.add_library_level,name="add_library_level"),
    path('edit_library_level/<int:pk>/',views.edit_library_level,name="edit_library_level"),
    path('add_shelf/<int:level_number>',views.add_shelf,name="add_shelf"),
    path('edit_shelf/<int:pk>/',views.edit_shelf,name="edit_shelf"), 
    path('stats/',views.stats,name="stats")
]