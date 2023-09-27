from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from .models import Todo
from .forms import UserForm
from .utils import *
from django.contrib.auth import authenticate, login
from .forms import LoginForm, TodoForm, DescriptionForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET, require_POST
from django.http import JsonResponse
from django.template.loader import render_to_string

@login_required
def todo_list(request, pk=None):
    context = {}
    super_todo = None
    if not pk is None:
        super_todo = get_object_or_404(Todo, pk=pk, user=request.user)
        context = {"super_todo": super_todo}

        if super_todo.super_todo:
            back_button_url = reverse("detail", kwargs={"pk": super_todo.super_todo.pk})
        else:
            back_button_url = reverse("todo_list")
        context["back_button_url"] = back_button_url

    context["uncompleted_todos"] = Todo.objects.filter(super_todo=super_todo, completed=False, user=request.user)
    context["completed_todos"] = Todo.objects.filter(super_todo=super_todo, completed=True, user=request.user)
    return render(request, "todo_list.html", context)

@require_not_address_bar
def add_description(request, pk):
    if request.method == "GET":
        form = DescriptionForm()
        context = {"action": reverse("add_desc", kwargs={"pk": pk}), "form": form}
        return render(request, "forms/description_add.html", context)
    else:
        todo = get_object_or_404(Todo, pk=pk, user=request.user)
        form = DescriptionForm(request.POST, instance=todo)
        if form.is_valid():
            todo.save()
            return JsonResponse({"redirect": reverse("detail", kwargs={"pk": todo.pk})})
        context = {"action": reverse("add_desc", kwargs={"pk": pk}), "form": form}
        return JsonResponse({"form": render_to_string("forms/description_add.html")})

@require_not_address_bar
def edit_description(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == "GET":
        form = DescriptionForm(instance=todo)
        context = {"action": reverse("edit_desc", kwargs={"pk": pk}), "form": form}
        return render(request, "forms/description_edit.html", context)
    else:
        form = DescriptionForm(request.POST, instance=todo)
        if form.is_valid():
            todo.save()
            return JsonResponse({"redirect": reverse("detail", kwargs={"pk": todo.pk})})
        context = {"action": reverse("edit_desc", kwargs={"pk": pk}), "form": form}
        return JsonResponse({"form": render_to_string("forms/description_edit.html")})


def complete(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if todo.completed:
        todo.completed = False
    else:
        complete_recursive(todo)
    todo.save()
    url = get_super_todo_url(todo)
    return redirect(url)


def delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.delete()
    url = get_super_todo_url(todo)
    return redirect(url)

@require_not_address_bar
def create_todo(request, pk=None):
    context = {"action": reverse("create", kwargs={"pk": pk}) if pk else reverse("create"),
               }
    if request.method == "GET":
        form = TodoForm()
        context["form"] = form
        return render(request, "forms/todo_create.html", context)
    else:
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            if pk:
                todo.super_todo = Todo.objects.get(pk=pk)
            todo.save()
            url = get_super_todo_url(todo)
            return JsonResponse({"redirect": url})
        context["form"] = form
        return JsonResponse({"form": render_to_string("forms/todo_create.html", context, request)})


class RegisterUserView(CreateView):
    model = User
    template_name = "register.html"
    form_class = UserForm
    success_url = reverse_lazy("todo_list")

    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'],
                            password=cd['password'])
        login(self.request, user)
        return result

class LoginView(LoginView):
    template_name = "login.html"
    form_class = LoginForm

def logout_user(request):
    logout(request)
    return redirect("login")

@require_not_address_bar
def edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    context = {}
    super_pk = None
    context = {"action": reverse("edit", kwargs={"pk": todo.pk})}
    if request.method == "GET":
        super_todo = todo.super_todo
        if super_todo:
            super_pk = super_todo.pk
        form = TodoForm(instance=todo)
        context["form"] = form
        return render(request, "forms/todo_edit.html", context)
    else:
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            if todo.super_todo:
                pk = todo.super_todo.pk
                return JsonResponse({"redirect": reverse("detail", kwargs={"pk":pk})})
            return JsonResponse({"redirect": reverse("todo_list")})
        context["form"] = form
        return JsonResponse({"form": render_to_string("forms/todo_edit.html", context, request)})
