from django.urls import path
import customer.views as cv

urlpatterns = [
    path("list/", cv.current_datetime),
]
