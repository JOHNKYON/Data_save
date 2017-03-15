# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import generators
from __future__ import nested_scopes
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import with_statement

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from Django.forms import CaptchaForm
import codecs


def home(request):
    captcha = CaptchaForm()
    return render_to_response('home.html', {'captcha': captcha})


def parameter_saver(request):
    output_file = codecs.open('data/data.txt', 'a', encoding='utf8')
    if request.GET:
        output_file.write(str(request.GET) + '\n')
        return HttpResponse("GET")
    elif request.POST:
        output_file.write(str(request.POST) + '\n')
        return HttpResponse("POST")
    output_file.close()
    return HttpResponse("Hello World!")


def captcha_verify(request):
    form = CaptchaForm(request.POST)
    if form.is_valid():
        return HttpResponseRedirect(request.path + '?ok')
    return HttpResponseRedirect(request.path + '?ok')
