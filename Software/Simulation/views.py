import logging
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.paginator import Paginator, InvalidPage ,EmptyPage
from django.core.urlresolvers import reverse
import hashlib
import random
import json
from django.core.mail import send_mail

@csrf_exempt
def front(request):
    return render_to_response('Simulation/algo.html')

@csrf_exempt
def quicksort(request):
    return render_to_response('Simulation/quicksort.html', {'user_permission':request.session['user_permission']})

@csrf_exempt
def mergesort(request):
    return render_to_response('Simulation/mergesort.html', {'user_permission':request.session['user_permission']})

@csrf_exempt
def shellsort(request):
    return render_to_response('Simulation/shellsort.html', {'user_permission':request.session['user_permission']})

@csrf_exempt
def bubblesort(request):
    return render_to_response('Simulation/bubblesort.html', {'user_permission':request.session['user_permission']})

@csrf_exempt
def selectionsort(request):
    return render_to_response('Simulation/selectionsort.html', {'user_permission':request.session['user_permission']})

@csrf_exempt
def insertionsort(request):
    return render_to_response('Simulation/insertionsort.html', {'user_permission':request.session['user_permission']})

@csrf_exempt
def sorttut(request):
	return render_to_response('Simulation/index.html')

@csrf_exempt
def dfs(request):
	return render_to_response('Simulation/dfs.html', {'user_permission':request.session['user_permission']})

@csrf_exempt
def bfs(request):
	return render_to_response('Simulation/bfs.html', {'user_permission':request.session['user_permission']})

@csrf_exempt
def dijkstra(request):
	return render_to_response('Simulation/dij.html', {'user_permission':request.session['user_permission']})

@csrf_exempt
def bellmann(request):
	return render_to_response('Simulation/bellman.html', {'user_permission':request.session['user_permission']})

@csrf_exempt
def kruskal(request):
	return render_to_response('Simulation/kruskal.html', {'user_permission':request.session['user_permission']})

@csrf_exempt
def prim(request):
	return render_to_response('Simulation/prim.html', {'user_permission':request.session['user_permission']})

@csrf_exempt
def graphtut(request):
	return render_to_response('Simulation/tutorial.html')

@csrf_exempt
def temp(request,filename):
	filename = filename.replace('/','.')
	with open('static/'+filename+'.json') as data_file:    
    		data = json.load(data_file)
	d = json.dumps(data)
	return HttpResponse(d,content_type="application/json")
	