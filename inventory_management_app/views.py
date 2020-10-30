from django.shortcuts import render


def first_page(request):
    template_name = "standard/intro.html"
    context = None
    return render(request, template_name, context)
