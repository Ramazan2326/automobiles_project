from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.index, name="index"),
    path("edit/<int:id>/", views.edit, name="edit"),
    path("delete/<int:id>/", views.delete, name="delete"),
    path('about-us/', views.about, name="about"),
    path('contacts/', views.contact, name="contact"),
    path('form/', views.create, name="create"),
    path('edit_db/', views.edit_page, name="edit_page"),
    path('edit_db/delete/<int:id>', views.delete, name = "delete"),
    path('edit_db/edit/<int:id>', views.edit, name = "edit"),
    path('downloadfile', views.downloadfile, name="downloadfile"),
]

