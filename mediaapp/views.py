from django.shortcuts import render, redirect
from .forms import MediaFileForm
from .models import MediaFile

def index(request):
    files = MediaFile.objects.all()
    return render(request, 'mediaapp/index.html', {'files': files})

def upload(request):
    if request.method == 'POST':
        form = MediaFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MediaFileForm()
    return render(request, 'mediaapp/upload.html', {'form': form})
