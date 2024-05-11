from rest_framework.serializers import Serializer, ModelSerializer
from .models import Sponsor, Student, StudentSponsor, Unversity, BaseModel
from rest_framework import serializers
from django.db.models import Sum



class SponsorSerializer(ModelSerializer):

    class Meta:
        model = Sponsor
        exclude = ('organization','updated_at','sponsor_type' )

class StudentSerializer(ModelSerializer):
    unversity = serializers.StringRelatedField(source='unversity.title')
    allocated_money = serializers.SerializerMethodField()

    def get_allocated_money(self, obj):
        return obj.all_data.all().aggregate(total_amount=Sum('amount'))['total_amount'] or 0

    
    class Meta:
        model = Student
        exclude = ('created_at','updated_at', 'phone' )

         


class StudentDetailSerializer(ModelSerializer):
    unversity = serializers.StringRelatedField(source='unversity.title')
    allocated_money = serializers.SerializerMethodField()

    def get_allocated_money(self, obj):
        return obj.all_data.all().aggregate(total_amount=Sum('amount'))['total_amount'] or 0
    
    class Meta:
        model = Student
        exclude = ('created_at','updated_at' )

class StudentSponsorSerializer(ModelSerializer):
    
    class Meta:
        model = StudentSponsor
        fields = ('id', 'student','sponsor','amount')
    def validate(self, attrs):
        amount = attrs.get('amount')
        sponsor = attrs.get('sponsor')
        student = attrs.get('student')
        from django.db.models import Sum
        student_paid_money = student.all_data.all().aggregate(total_amount=Sum('amount'))['total_amount'] or 0
        if student.contract_amount - student_paid_money < amount:
            raise serializers.ValidationError(detail={'error': f'siz {student.contract_amount - student_paid_money} ortiqcha to\'ladiz '})
        sponsor_paid_money = sponsor.all_data.all().aggregate(total_amount=Sum('amount'))['total_amount'] or 0
        if sponsor.sum - sponsor_paid_money  < amount:
            raise serializers.ValidationError(detail={'error': f'sizda {sponsor_paid_money - sponsor.sum} bor holis'})

        return super().validate(attrs)

















