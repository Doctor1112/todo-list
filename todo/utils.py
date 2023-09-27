from django.shortcuts import reverse, redirect

def complete_recursive(todo):
    todo.completed = True
    todo.save()
    for sub_todo in todo.todos.all():
        complete_recursive(sub_todo)

def require_not_address_bar(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.META.get('HTTP_REFERER'):
            return view_func(request, *args, **kwargs)
        else:
            return redirect("todo_list")
    return _wrapped_view

def get_super_todo_url(todo):
    pk = None
    super_todo = todo.super_todo
    if super_todo:
        return reverse('detail', kwargs={"pk": super_todo.pk})
    return reverse('todo_list')