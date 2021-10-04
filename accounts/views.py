from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from wheelspin.models import RefferUser
# Create your views here.

@login_required
def index(request):
    return render(request,'wheelspin/profile.html')
def sign_up(request):
    profile_id = request.session.get('ref_profile')
    print(profile_id)
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            
            try:
                recommended_by_profile = RefferUser.objects.get(id=profile_id)
                print("rbp: ", str(recommended_by_profile))
                registered_user = User.objects.get(id=user.id)
                print('ru: ', str(registered_user))
                registered_profile = RefferUser.objects.get(user=registered_user)
                print("rp: ", str(registered_profile))
                registered_profile.ref_by = recommended_by_profile.user
                print(registered_profile.ref_by)
                registered_profile.save()
                print("refer added")
            except:
                print("Error occured")

            login(request,user)
            return redirect(index)
            
    context['form']=form
    return render(request,'registration/sign_up.html',context)
