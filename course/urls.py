from django.urls import path
from .views import CourseView
from .views import CourseDetailView
app_name = "courses"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('courses/', CourseView.as_view(), name='coursesList'),
    path('courses/<int:pk>', CourseDetailView.as_view(),name='courseDetail')
]