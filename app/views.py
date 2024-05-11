from django.shortcuts import render
from rest_framework.views import APIView, Response
from .models import Sponsor, Student, StudentSponsor
from .serializer import SponsorSerializer, StudentSerializer, StudentSponsorSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView,ListAPIView, DestroyAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class SponsorCreatreAPIview(CreateAPIView):
    serializer_class = SponsorSerializer
    queryset = Sponsor.objects.all()

class SponsorUpdateAPIview(UpdateAPIView):
    serializer_class = SponsorSerializer
    queryset = Sponsor.objects.all()

class SponsorListAPIview(ListAPIView):
    serializer_class = SponsorSerializer
    queryset = Sponsor.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('conditions',)
    search_fields = ('full_name','payment_type')


class StudentUpdateAPIview(UpdateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class StudentListAPIview(ListAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('student_type','unversity',)
    search_fields = ('full_name',)

class StudentRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()



class StudentSponsorCreatreAPIview(CreateAPIView):
    serializer_class = StudentSponsorSerializer
    queryset = StudentSponsor.objects.all()






# class SonsorAPIView(APIView):

#     def get(self, request, *args, **kwargs):
#         sponsor = Sponsor.objects.all()
#         serializer = SponsorSerializer(sponsor, many=True)
#         return Response(serializer.data)
    

# class StudentAPIView(APIView):

#     def get(self, request, *args, **kwargs):
#         student = Student.objects.all()
#         serializer = StudentSerializer(student, many=True)
#         return Response(serializer.data)