from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import MasterRegistrationForm

def register(request):
    if request.method == 'POST':
        master_form = MasterRegistrationForm(requeset.POST)
        if master_form.is_valid():
            # Create a new master without commiting to DB
            new_master = user_form.save(commit=False)
            # Set a password with a proper encryption scheme
            new_master.set_password(
                master_form.cleaned_data['password'])
            new_master.save()
            return render(request,
                          'master/register_done.html',
                          {'new_master': new_master})
    else:
        master_form = MasterRegistrationForm()
    return render(request,
                  'master/register.html',
                  {'master_form': master_form})

# @login_required
# def edit(request):
#     if request.method == 'POST':
#         user_form = UserEditForm(instance=request.user,
#                                  data=request.POST)
#         profile_form = ProfileEditForm(instance=request.user.profile,
#                                        data=request.POST,
#                                        files=request.FILES)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Profile updated successfully')
#         else:
#             messages.error(request, 'Error updating your profile')
#     else:
#         user_form = UserEditForm(instance=request.user)
#         profile_form = ProfileEditForm(instance=request.user.profile)
#     return render(request, 'account/edit.html', {'user_form': user_form,
#                                                  'profile_form': profile_form})
#

@login_required
def dashboard(request):
    return render(request, 'master/dashboard.html', {'section': 'dashboard'})
