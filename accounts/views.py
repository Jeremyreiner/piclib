from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth
from django.views.generic import DetailView, UpdateView
from photos.models import  Photo

from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Profile
from django.contrib.auth.decorators import login_required


from django.db.models import Q

# Create your views here.

def registration(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is currently being used')
                    return redirect('register')
                else:
                    user= User.objects.create_user(
                        username=username,
                        password=password,
                        email=email,
                        first_name=first_name,
                        last_name=last_name
                    )
                    user.save()
                    user = authenticate(username= username, password=password2)
                    if user is not None:
                        print('User is authenticated')
                        login(request)
                        messages.success(request, 'You are now registered and can log in')
                        return redirect('gallery')
                    else:
                        print('user is NOT authenticated')
                        return redirect('register')
        else:
            messages.error(request, 'Either username/passwords did not match')
            return redirect('register')

    else:
        return render(request, 'accounts/registeration.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Succesfully logged in')
            return redirect('gallery')
        else:
            messages.error(request, 'Either incorrect username or password. Try again')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method =='POST':
        auth.logout(request)
        messages.success(request, 'You have been logged out')
        return redirect('gallery')


class UserDetailView(DetailView):

    template_name = 'accounts/profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()

    content_object_name ='profile'

    def get_context_data(self,*args, **kwargs):
        context = super(UserDetailView, self).get_context_data(*args, **kwargs)
        profile = self.get_object()
        context['photos'] = Photo.objects.filter(profile=profile).order_by('-timestamp')
        return  context


@login_required
def ProfileUpdate(request, username):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'The updates to your account have been applied')
            return redirect('user_profile', username)
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'accounts/update_profile.html', context)


# def search_photos(request):
#     if request.method == "POST":
#         searched = request.POST['searched']
#         photos = Photo.objects.filter(
#             Q(name__icontains = searched) |
#             Q(description__icontains = searched)
#         )

#         context = {
#             'searched': searched,
#             'photos':photos
#         }
#         return render(request, 'photos/search.html', context)
#     else:
#         return render(request, 'photos/search.html')