from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, AddAccountForm
from .models import Master

def register(request):
    if request.method == 'POST':
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            # A master will be associated with a user
            new_master = Master()
            # Create a new user without commiting to DB
            new_user = reg_form.save(commit=False)
            # Set a password with a proper encryption scheme
            new_user.set_password(
                reg_form.cleaned_data['password'])
            new_user.save()

            new_master.user = new_user
            new_master.nickname = reg_form.cleaned_data['nickname']
            new_master.save()

            return render(request,
                          'master/register_done.html',
                          {'new_master': new_master})
    else:
        reg_form = RegistrationForm()
    return render(request,
                  'master/register.html',
                  {'reg_form': reg_form})

@login_required
def dashboard(request):
    master = request.user.master
    accounts = master.accounts.all()
    return render(request, 'master/dashboard.html',
                  {'section': 'dashboard',
                   'accounts': accounts})

@login_required
def add_account(request):
    if request.method == 'POST':
        account_form = AddAccountForm(request.POST)
        if account_form.is_valid():
            account = account_form.save(commit=False)
            account.master = request.user.master
            account.save()
    else:
        account_form = AddAccountForm(request.POST)
    return render(request, 'master/add_account.html',
                  {'account_form': account_form})


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
