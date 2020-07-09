from rest_framework import serializers
from .models import Data_mahasiswa

class MahasiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data_mahasiswa
        fields = '__all__'