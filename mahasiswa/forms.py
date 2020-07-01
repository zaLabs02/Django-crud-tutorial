
from django import forms
from .models import Data_mahasiswa

class BiodataMhs(forms.ModelForm):
    class Meta:
        model = Data_mahasiswa
        fields = "__all__"
        error_messages = {
            'npm': {
                'required': 'Anda harus mengisi form NPM'
            },
            'nama' : {
                'required': "Anda harus mengisi form Nama"
            },
            'tgl_lahir' : {
                'required': "Anda harus menset form Tanggal lahir"
            },
            'alamat':{
                'required': "Anda harus mengisi form Alamat"
            }
        }