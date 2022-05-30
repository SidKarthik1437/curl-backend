from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutes, name="routes"),
    path("scripts/", views.getScripts, name="scripts"),
    path("scripts/create/", views.createScript, name="create-script"),
    path("scripts/<str:pk>/update/", views.updateScript, name="update-script"),
    path("scripts/<str:pk>/delete/", views.deleteScript, name="delete-script"),
    path("scripts/<str:pk>/execute/", views.executeScript, name="execute-script"),
    path("file/upload/", views.uploadFile, name="upload-file"),
    path("files/", views.getFiles, name="files"),
    path("scripts/<str:pk>/", views.getScript, name="script"),

]
