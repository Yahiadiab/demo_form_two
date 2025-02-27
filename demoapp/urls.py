from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_view, name="Form_Model"),
    path('delete/<int:entry_id>/', views.delete_entry, name="delete_entry"),
    path('update/<int:entry_id>/', views.update_entry, name="update_entry"),

]
