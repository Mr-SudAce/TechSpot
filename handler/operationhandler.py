from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import *

def handle_create(
        request,
        model,
        formname,
        redirect_url,
        template_url,
        action_url
    ):
    data = model.objects.order_by('-id')
    if request.method == "POST":
        form = formname(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = formname()
    context = {
        "form": form,
        "data": data,
        'action_url': reverse(action_url)
        }
    return render(request, template_url, context)

# update

def handle_update(
    request,
    id,
    model,
    formname,
    redirect_url,
    template_url,
    action_url
):
    data = get_object_or_404(model, id=id)
    if request.method == 'POST':
        form = formname(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = formname(instance=data)
    context = {
        "form": form,
        "data": model.objects.order_by('-id'),
        'action_url': reverse(action_url, args=[id]),
    }

    return render(request, template_url, context)




# Delete
def handle_delete(
        request,
        id,
        model,
        redirect_url,
        success_msg
    ):
    item = get_object_or_404(model, id=id)
    item.delete()
    messages.success(request, success_msg)
    return redirect(redirect_url)

