from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView, UpdateView
from .models import Category, Photo, Comment
from accounts.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView
from django.contrib.auth.models import User

from django.db.models import Q
# Create your views here.
def about(request):
    return render(request, 'photos/about.html')


def gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all().order_by("-timestamp")
    else:
        photos = Photo.objects.filter(category__name=category).order_by("-timestamp")

    categories= Category.objects.all()
    context = {
        'categories': categories,
        'photos': photos,
    }
    return render(request, 'photos/gallery.html', context)


def search_photos(request):
    if request.method == "POST":
        searched = request.POST['searched']
        photos = Photo.objects.filter(
            Q(name__icontains = searched) |
            Q(description__icontains = searched)
        )

        context = {
            'searched': searched,
            'photos':photos
        }
        return render(request, 'photos/search.html', context)
    else:
        return render(request, 'photos/search.html')

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
                name = data['name'],
                category = category,
                image = image,
            )
        return redirect('gallery')


    context = {
        'categories': categories,
    }
    return render(request, 'photos/add_image.html', context)


class PhotoUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Photo
    fields= ['name', 'category', 'description', 'image']
    template_name="photos/update_photo.html"

    def form_valid(self, form):
        form.instance.profile = self.request.user
        return super().form_valid(form)

    def test_func(self):
        photo= self.get_object()
        if self.request.user == photo.profile:
            return True
        return False
    


class PhotoDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Photo
    context_object_name = 'photo'
    success_url= '/'

    def test_func(self):
        photo= self.get_object()
        if self.request.user == photo.profile:
            return True
        return False


class CategoryDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Category
    context_object_name = 'category'
    success_url= '/'

    def test_func(self):
        category= self.get_object()
        if self.request.user == self.request.user: #make this only a staff option
            return True
        return False


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

