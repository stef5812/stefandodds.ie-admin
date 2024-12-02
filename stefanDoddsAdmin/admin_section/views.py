from django.shortcuts import render, redirect
from .forms import ContactForm, GalleryForm
from .models import GalleryImage

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'admin_section/contact.html', {'form': form})

def gallery_view(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery_success')
    else:
        form = GalleryForm()
    images = GalleryImage.objects.all()
    return render(request, 'admin_section/gallery.html', {'form': form, 'images': images})

def gallery_success_view(request):
    return render(request, 'admin_section/gallery_success.html')

# views.py
from django.shortcuts import render

def dynamic_content(request):
    return render(request, 'admin_section/contact.html')
