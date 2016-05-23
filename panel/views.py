from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django import forms
from panel.models import file_zone

class UserForm(forms.Form):
    username = forms.CharField()
    userfile = forms.FileField()


def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST, request.FILES)
        if uf.is_valid():
            userID = uf.cleaned_data['username']
            fileName = uf.cleaned_data['userfile']
            user = file_zone()
            user.userID = userID
            user.fileName = fileName
            user.save()
            return HttpResponse('upload OK!')
    else:
        uf = UserForm()
    html = render_to_response('register.html',{'uf':uf})
    return HttpResponse(html)