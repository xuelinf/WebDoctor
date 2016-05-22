from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django import forms

class UserForm(forms.Form):
    username = forms.CharField()
    userfile = forms.FileField()


def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST, request.FILES)
        if uf.is_valid():
            return HttpResponse('upload OK!')
    else:
        uf = UserForm()
    html = render_to_response('register.html',{'uf':uf})
    return HttpResponse(html)