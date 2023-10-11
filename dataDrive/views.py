import os

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from constants import STATUS_ACTIVE
from dataDrive.forms import UserForm
from dataDrive.models import CustomUser, Folder, File


def log_in(request):
    """Allows user to login to the system if already registered."""
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                employee_data = CustomUser.objects.filter(user=user).first()
                if employee_data.status == 'Active':
                    login(request, user)
                    return redirect('index')
                else:
                    return render(request, 'dataDrive/login.html',
                                  {'error_message': 'Your account has been disabled'})
            else:
                return render(request, 'dataDrive/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'dataDrive/login.html', {'error_message': 'Invalid login'})
    return render(request, 'dataDrive/login.html')


def logout_user(request):
    """Logout an already logged in user."""
    if not request.user.is_authenticated:
        return redirect('login')

    logout(request)
    return render(request, 'dataDrive/logout.html')


def register(request):
    """Method for registering a new user."""
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        try:
            user = User.objects.create_user(username=username, email=email, password=password)

            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
            employee = CustomUser(user=user, status=STATUS_ACTIVE)
            employee.save()

            return HttpResponse('Success::' + "User registered successfully.")
        except Exception as e:
            return HttpResponse("There is some error. Please try again" + str(e))
    return render(request, 'dataDrive/register.html')


def index(request):
    """It is the default page where the user will find it all base folder and files.
    Here user can also manage its folder and files. Like add, update and delete."""
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "GET":
        all_folders = Folder.objects.filter(custom_user__user=request.user, parent_folder=None).all()
        all_files = File.objects.filter(custom_user__user=request.user, parent_folder=None).all()

        context = {
            'all_folders': all_folders, 'all_files': all_files, 'add_data_table_support': True,
            'add_loading_animation': True
        }
        return render(request, 'dataDrive/index.html', context)

    if request.method == "POST":
        action = request.POST['action']
        custom_user = CustomUser.objects.filter(user=request.user).first()

        if action == "Add Folder":
            try:
                folder_name = request.POST['folder_name']

                new_folder = Folder(name=folder_name, custom_user=custom_user, parent_folder=None)
                new_folder.save()
                return HttpResponse('Success::' + "Folder added successfully.")
            except Exception as e:
                return HttpResponse("There is some error. Please try again" + str(e))

        if action == "Edit Folder":
            try:
                folder_id = request.POST['folder_id']
                folder_name = request.POST['folder_name']

                folder = Folder.objects.filter(id=folder_id, custom_user=custom_user, parent_folder=None).first()
                folder.name = folder_name
                folder.save()
                return HttpResponse('Success::' + "Folder name updated successfully.")
            except Exception as e:
                return HttpResponse("There is some error. Please try again" + str(e))

        if action == "Delete Folder":
            try:
                folder_id = request.POST['folder_id']

                Folder.objects.filter(id=folder_id, custom_user=custom_user, parent_folder=None).delete()
                return HttpResponse('Success::' + "Folder deleted successfully.")
            except Exception as e:
                return HttpResponse("There is some error. Please try again" + str(e))

        if action == "Add File":
            try:
                selected_file = request.FILES['selected_file']

                new_file = File(file=selected_file, custom_user=custom_user, parent_folder=None)
                new_file.save()
                return HttpResponse('Success::' + "File added successfully.")
            except Exception as e:
                return HttpResponse("There is some error. Please try again" + str(e))

        if action == "Delete File":
            try:
                file_id = request.POST['file_id']

                existing_file = File.objects.filter(id=file_id, custom_user=custom_user, parent_folder=None).first()

                old_file = str(existing_file.file)
                if old_file:
                    os.remove('media/' + old_file)
                existing_file.delete()
                return HttpResponse('Success::' + "File deleted successfully.")
            except Exception as e:
                return HttpResponse("There is some error. Please try again" + str(e))

    context = {}
    context.update({'add_data_table_support': True})
    context.update({'add_loading_animation': True})
    return render(request, 'dataDrive/index.html', context)


def view_folder(request, _id):
    """Here the user can view its data within a folder. User can also manage its folder and files.
    Like add, update and delete."""
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "GET":
        all_folders = Folder.objects.filter(custom_user__user=request.user, parent_folder_id=_id).all()
        all_files = File.objects.filter(custom_user__user=request.user, parent_folder_id=_id).all()

        context = {
            'all_folders': all_folders, 'all_files': all_files, 'add_data_table_support': True,
            'add_loading_animation': True, 'folder_id': _id
        }
        return render(request, 'dataDrive/view_folder.html', context)

    if request.method == "POST":
        action = request.POST['action']
        custom_user = CustomUser.objects.filter(user=request.user).first()

        if action == "Add Folder":
            try:
                folder_name = request.POST['folder_name']

                new_folder = Folder(name=folder_name, custom_user=custom_user, parent_folder_id=_id)
                new_folder.save()
                return HttpResponse('Success::' + "Folder added successfully.")
            except Exception as e:
                return HttpResponse("There is some error. Please try again" + str(e))

        if action == "Edit Folder":
            try:
                folder_id = request.POST['folder_id']
                folder_name = request.POST['folder_name']

                folder = Folder.objects.filter(id=folder_id, custom_user=custom_user, parent_folder_id=_id).first()
                folder.name = folder_name
                folder.save()
                return HttpResponse('Success::' + "Folder name updated successfully.")
            except Exception as e:
                return HttpResponse("There is some error. Please try again" + str(e))

        if action == "Delete Folder":
            try:
                folder_id = request.POST['folder_id']

                Folder.objects.filter(id=folder_id, custom_user=custom_user, parent_folder_id=_id).delete()
                return HttpResponse('Success::' + "Folder deleted successfully.")
            except Exception as e:
                return HttpResponse("There is some error. Please try again" + str(e))

        if action == "Add File":
            try:
                selected_file = request.FILES['selected_file']

                new_file = File(file=selected_file, custom_user=custom_user, parent_folder_id=_id)
                new_file.save()
                return HttpResponse('Success::' + "File added successfully.")
            except Exception as e:
                return HttpResponse("There is some error. Please try again" + str(e))

        if action == "Delete File":
            try:
                file_id = request.POST['file_id']

                existing_file = File.objects.filter(id=file_id, custom_user=custom_user, parent_folder_id=_id).first()

                old_file = str(existing_file.file)
                if old_file:
                    os.remove('media/' + old_file)
                existing_file.delete()
                return HttpResponse('Success::' + "File deleted successfully.")
            except Exception as e:
                return HttpResponse("There is some error. Please try again" + str(e))

    context = {}
    context.update({'add_data_table_support': True})
    context.update({'add_loading_animation': True})
    return render(request, 'dataDrive/view_folder.html', context)
