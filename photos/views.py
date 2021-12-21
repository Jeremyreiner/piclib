from django.shortcuts import render, redirect
from .models import Category, Photo

# Create your views here.
def gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories= Category.objects.all()
    context = {
        'categories': categories,
        'photos': photos
    }
    return render(request, 'photos/gallery.html', context)


def SinglePhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    context = {
        'photo': photo,
    }
    return render(request, 'photos/single_photo.html', context)


def AddImage(request):
    categories= Category.objects.all()
    
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('Upload_images')

        if data['category'] != 'none':
            category= Category.objects.get(id=data['category'])
        elif data['new_category'] != '':
            category, created = Category.objects.get_or_create(name=data['new_category'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                description = data['description'],
                category = category,
                image = image,
            )
        return redirect('gallery')


    context = {
        'categories': categories,
    }
    return render(request, 'photos/add_image.html', context)