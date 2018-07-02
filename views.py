# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime


def time(request):
  context = {
  		#sets key/value pair to be used as static in HTML template.
  		"time": strftime("%Y-%m-%d %H:%M %p", gmtime())
  }
  #request name, app name, html template, context.
  return render(request,'time_display/index.html', context)

