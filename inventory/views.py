from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import ObjectForm
from .models import Object


@login_required
def list_objects(request):
    list_of_objects = Object.objects.filter(user=request.user)
    template_name = "inventory/list.html"
    context = {"list_of_objects": list_of_objects}
    return render(request, template_name, context)


@login_required
def single_object(request, slug):
    obj = Object.objects.get(slug=slug)
    template_name = "inventory/detail.html"
    context = {"object": obj}
    return render(request, template_name, context)


@login_required
def create(request):
    form = ObjectForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = ObjectForm()
        return redirect('/inventory/all/')
    template_name = "inventory/create.html"
    context = {"form": form}
    return render(request, template_name, context)


@login_required
def update(request, slug):
    obj = get_object_or_404(Object, slug=slug)
    template_name = "inventory/update.html"
    form = ObjectForm(request.POST or None, instance=obj)
    context = {"form": form}
    if form.is_valid():
        form.save()
        return redirect('/inventory/all')
    return render(request, template_name, context)


@login_required
def delete(request, slug):
    obj = get_object_or_404(Object, slug=slug)
    template_name = "inventory/delete.html"
    if request.method == "POST":
        obj.delete()
        return redirect("/inventory/all/")
    context = {"object": obj}
    return render(request, template_name, context)
