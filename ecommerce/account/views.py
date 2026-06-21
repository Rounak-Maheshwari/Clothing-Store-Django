from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegisterForm, ProfileForm, AddressForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile, Address

# Create your views here.
def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            profile.save()
            messages.success(request, 'Account created successfully.')
            return redirect('account-login')
        else:
            messages.error(request, 'Something went wrong. Try again!')
    else:
        form = RegisterForm()

    return render(request, 'account/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=username, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged In Successfully!")
            return redirect('account-profile')
        else:
            messages.error(request, 'Invalid Credentials. Try again')

    return render(request, 'account/login.html')

@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, 'Logged out successfully')
        return redirect('account-login')

    return render(request, 'account/logout.html')


def forgot_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        user = authenticate(request, username=username, email=email)
        if user is not None:
            if password1 == password2:
                user.set_password = password1
                user.save()
                messages.success('Password has reset successfully! ')
                return redirect('account-login')
        
        else:
            messages.error(request, 'Something went wrong! Try again')
    
    return render(request, 'account/forgot_password.html') 

@login_required
def profile_view(request):

    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()

            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')

            user = request.user
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            messages.success(request, "Profile updated successfully!")
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'account/profile.html', {'form': form})


@login_required
def all_addresses(request):
    addresses = Address.objects.filter(user=request.user)

    return render(request, 'account/addresses.html', {'addresses': addresses})

@login_required
def add_new_address(request):

    if request.method == 'POST':
        form = AddressForm(request.POST)

        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            messages.success(request, "New address added Successfully!")
            return redirect('account-profile-address')
        else:
            messages.error(request, "Something went wrong!")
    else:
        form = AddressForm()

    return render(request, 'account/address_form.html', {'form': form})


@login_required
def delete_address(request, id):

    if request.method == 'POST':
        addresses = Address.objects.filter(user=request.user)
        address = addresses.get(id=id)

        address.delete()
        messages.success(request, 'Address deleted successfully')
    
    return redirect('account-profile-address')

@login_required
def edit_address(request, id):

    addresses = Address.objects.filter(user=request.user)
    address = addresses.get(id=id)

    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)

        if form.is_valid():
            form.save()
            messages.success(request, 'Address updated successfully!')
            return redirect('account-profile-address')
        else:
            messages.success(request, 'Something went wrong!')
    else:
        form = AddressForm(instance=address)

    return render(request, 'account/address_form.html', {'form': form})
