#coding: utf-8
__author__ = 'xuelinf'

from django.shortcuts import render_to_response
from django.http import HttpResponse

def demo(request):
    html = render_to_response('demo.html',{})
    return HttpResponse(html)