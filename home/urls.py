from django.contrib import admin
from django.urls import path
from .import views


admin.site.header="Developer Bony Born"
admin.site.site_title="Welcome to Bony's Dashboard"
admin.site.index_title="Welcome to this Portal"

urlpatterns=[
    path("", views.home, name="home"),
    path("about/", views.home, name="about"),
    path("project", views.home, name="project"),
    path("contact", views.home, name="contact"),
]

