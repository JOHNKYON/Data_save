# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import generators
from __future__ import nested_scopes
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import with_statement

from django.http import HttpResponse
from django.shortcuts import render_to_response

import codecs


def test_transfer(request):
    return render_to_response('test_page.html')


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