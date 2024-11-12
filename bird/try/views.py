from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import ImageUpload

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_images')
    else:
        form = ImageUploadForm()
    return render(request, 'try/upload_image.html', {'form': form})

def view_images(request):
    images = ImageUpload.objects.all()
    return render(request, 'try/view_images.html', {'images': images})
