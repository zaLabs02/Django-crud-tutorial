from django.shortcuts import render, redirect, get_object_or_404
from .models import Data_mahasiswa
from .forms import BiodataMhs
# Create your views here.

def index(request):
    hasil = Data_mahasiswa.objects.all()
    print(hasil)
    data = {
        'data':hasil,
    }   
    return render(request,"index.html",data)

def tambah(request):
    form = BiodataMhs(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        # formny = BiodataMhs(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        pass
    return render(request,"tambahdata.html",{'form': form})

def edit(request, npm):
    obj = get_object_or_404(Data_mahasiswa, npm = npm) 
  
    form = BiodataMhs(request.POST or None, instance = obj)
    if form.is_valid(): 
        form.save() 
        return redirect("/")  
    data = {
        'mhs':obj,
    }
    return render(request, 'editdata.html',data)

def hapus(request, npm):
    dt = Data_mahasiswa.objects.get(npm=npm)
    dt.delete()
    return redirect("/")