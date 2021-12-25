from django.shortcuts import render,redirect

# Create your views here.
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from  .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm

def register(request):
    # form = UserRegisterForm(request.POST)
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'yangi akkount yaratildi. Siz login qila olasiz')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Sizning akkauntingiz yangilandi')
            return redirect('profile')

    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)

    context={
        'u_form':u_form,
        'p_form':p_form
    }            
    return render(request, 'users/profile.html',context)