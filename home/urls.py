from django.contrib import admin
from django.urls import path
from .import views


admin.site.site_header="Developer Bony Born's Administration"
admin.site.site_title="Adm B.B™"
admin.site.index_title="Admin BonyBorn"

urlpatterns=[
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("projects/", views.project, name="projects"),
    path("contact/", views.contact, name="contact-me"),
]

