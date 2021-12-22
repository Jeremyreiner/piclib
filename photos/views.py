from django.shortcuts import render, redirect
from .models import Category, Photo, Comment
from accounts.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.contrib.auth.models import User
# Create your views here.
def about(request):
    return render(request, 'photos/about.html')


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
    profile = Profile.objects.filter(user=request.user)
    
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
                profile = request.user,
                description = data['description'],
                category = category,
                image = image,
            )
        return redirect('gallery')


    context = {
        'categories': categories,
    }
    return render(request, 'photos/add_image.html', context)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content',]
    template_name = 'photos/new_comment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photo'] = Photo.objects.get(id=self.kwargs['photo_id'])
        return context

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.owner = self.request.user
        photo_id = self.kwargs['photo_id']
        photo = Photo.objects.get(id=photo_id)
        comment.photo = photo
        comment.save()
        return super().form_valid(form)