from django.urls import path
from .views import SponsorCreatreAPIview, SponsorListAPIview,SponsorUpdateAPIview
from .views import StudentSponsorCreatreAPIview, StudentListAPIview, StudentUpdateAPIview,StudentRetrieveUpdateAPIView, StatisticsAPIVeiw, graphAPIView
urlpatterns = [
    path('sponsor-list/', SponsorListAPIview.as_view()),
    path('sponsor-create/', SponsorCreatreAPIview.as_view()),
    path('sponsor-update/', SponsorUpdateAPIview.as_view()),

    path('student-list/', StudentListAPIview.as_view()),
    path('student-list/<int:pk>', StudentRetrieveUpdateAPIView.as_view()),
    path('student-create/', StudentSponsorCreatreAPIview.as_view()),
    path('student-update/<int:pk>', StudentUpdateAPIview.as_view()),

    path('student-sponsor-create/', StudentSponsorCreatreAPIview.as_view()),

    path('amount-statistic', StatisticsAPIVeiw.as_view()),
    path('graph', graphAPIView.as_view())
]