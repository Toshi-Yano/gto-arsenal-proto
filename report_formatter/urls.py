from django.urls import path

from . import views

app_name = "report_formatter"
urlpatterns = [
    path("", views.FileUploadView.as_view(), name="file-upload"),
]
