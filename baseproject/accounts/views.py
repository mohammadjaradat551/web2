from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Profile
from property.models import PropertyBook, Property

# Create your views here.

def signup(request):
    if request.method == 'POST':
        signup_form = UserCreateForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            #return redirect(reverse('accounts:login'))
            #سيمنع cleaned_data[] إدخال اسم مستخدم مكرر.
            username= signup_form.cleaned_data["username"]
            password= signup_form.cleaned_data["password1"]
            user= authenticate(username= username, password= password)
            login(request, user)
            return redirect(reverse('accounts:profile'))
    else :
        signup_form = UserCreateForm()
    return render(request, 'registration/signup.html', {'signup_form':signup_form})

def add_list(request):
    form= AddListForm()
    if request.method == 'POST':
        form= AddListForm(request.POST, request.FILES)
        # assign the owner attribute here
        form.instance.owner= request.user
        print('check valid')

        if form.is_valid():
            print('valid')
            form.save()
            return redirect('accounts:profile')
        else:
            # print the form errors here
            print(form.errors)
    else:
        form= AddListForm()

    return render(request, 'add_list.html', {'form':form})


def sign_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse('accounts:profile'))
        login_form = LoginForm()
        return render(request, 'registration/login.html', {'login_form': login_form})
    
    elif request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            print('login_form.errors')
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi  welcome back!')
                
                return redirect(reverse('accounts:profile'))
        else:
            print(login_form.errors)
        
        messages.error(request,f'Invalid username or password')
        return render(request,'registration/login.html',{'login_form': login_form})
    else :
        login_form = LoginForm()
    return render(request, 'registration/login.html', {'login_form': login_form})





def profile(request):
    profile = Profile.objects.get(user= request.user)
    return render(request, 'profile/profile.html', {'profile':profile})





def my_reservations(request):
    my_reservations= PropertyBook.objects.filter(user=request.user)
    return render(request, 'profile/my_reservation.html', {'my_reservations':my_reservations})






def my_listing(request):
    my_list= Property.objects.filter(owner= request.user)
    return render(request, 'profile/my_listing.html', {'my_list':my_list})










def edit_profile(request):
    profile= Profile.objects.get(user= request.user)
    if request.method == 'POST':
        user_form= UserForm(request.POST, instance= request.user)
        profile_form= ProfileForm(request.POST,request.FILES, instance= profile)
        if user_form.is_valid and profile_form.is_valid():
            user_form.save()
            my_form= profile_form.save(commit= False)
            my_form.user = request.user
            my_form.save()
            messages.success(request, 'Profile details updated.')
            return redirect(reverse('accounts:profile'))

    else:
        user_form= UserForm(instance= request.user)
        profile_form= ProfileForm(instance= profile)
    return render(request, 'profile/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })




#its wrong, didint work
def password_reset(request):
    if request.method == 'POST':
        reset_form= PasswordResetForm(request.POST)
        if reset_form.is_valid():
            reset_form.save()
            return redirect(reverse('accounts:password_reset'))
    else :
        reset_form= PasswordResetForm()
    return render(request, 'registration/password_reset.html', {'reset_form':reset_form})
