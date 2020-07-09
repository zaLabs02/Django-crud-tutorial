from rest_framework import viewsets
from .models import Data_mahasiswa
from .serializers import MahasiswaSerializer

class DataMhsViewset(viewsets.ModelViewSet):
    queryset = Data_mahasiswa.objects.all()
    serializer_class = MahasiswaSerializer