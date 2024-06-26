from django.shortcuts import render
from rest_framework.views import APIView, Response
from .models import Sponsor, Student, StudentSponsor
from .serializer import SponsorSerializer, StudentSerializer, StudentSponsorSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView,ListAPIView, DestroyAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.db.models import Sum
from datetime import datetime



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



class StatisticsAPIVeiw(APIView):

    def get(self, request):
        total_paid_amount = StudentSponsor.objects.all().aggregate(total=Sum('amount'))['total'] or 0
        total_required_amount = Student.objects.all().aggregate(total=Sum('contract_amount'))['total'] or 0
        total_unpaid_amount = total_required_amount - total_paid_amount

        return Response(
            data={
                "total_paid_amount": total_paid_amount,
                "total_required_amount": total_required_amount,
                "total_unpaid_amount": total_unpaid_amount
            }
        )

class graphAPIView(APIView):
    
    def get(self, request):
        this_year = datetime.now().year
        result = []

        for i in range(1,13):
            spomsor_amount = Sponsor.objects.filter(
                created_at__month = i,
                created_at__year = this_year,
                conditions = 'tasdiqlangan'
            ).aggregate(total=Sum('sum'))['total'] or 0

            student_amout = Student.objects.filter(
                created_at__month = i,
                created_at__year = this_year
            ).aggregate(total=Sum('contract_amount'))['total'] or 0
            result.append({
                'month': i,
                'spomsor_amount':spomsor_amount,
                'student_amout':student_amout,
            })
        return Response(result)
