import logging
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from Article.models import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.paginator import Paginator, InvalidPage ,EmptyPage
from django.core.urlresolvers import reverse
import hashlib
import random
from django.core.mail import send_mail

@csrf_exempt
def edit_profile(request):
   
        if request.session['id'] != "" :
            if(request.session['user_permission']==-1) : 
		        return HttpResponseRedirect('/articles/all/')	
            if 'save' in request.POST :
                data = MyUser.objects.get(user_name=request.session['id'])
                setattr(data, "user_email", request.POST['email'])
                setattr(data, "user_college", request.POST['college'])
                #setattr(data, "photo", request.FILES['file'])
                request.session['user_email'] = request.POST['email']
                request.session['user_college'] = request.POST['college']  
                data.save()
                return render_to_response('MyUser/edit_profile.html',{'success':"Credentials are successfully updated.",'email':request.session['user_email'],'college':request.session['user_college'],'myuser':data,'user_permission':request.session['user_permission']})

            if 'change_password' in request.POST :
            	data = MyUser.objects.get(user_name=request.session['id'])
            	old_pwd = getattr(data, "user_password")
            	curr_pwd = request.POST.get('curr_password')
            	new_pwd = request.POST.get('new_password')
            	conf_pwd = request.POST.get('conf_password')
            
            	if old_pwd != curr_pwd:
                	error = "Current Password not matched"
                	return render_to_response('MyUser/edit_profile.html', {'error': error,'email':request.session['user_email'],'college':request.session['user_college'],'myuser':data,'user_permission':request.session['user_permission']})

            	if new_pwd != conf_pwd:
                	error = "New and Confirm Password not matched"
                	return render_to_response('MyUser/edit_profile.html', {'error': error,'email':request.session['user_email'],'college':request.session['user_college'],'myuser':data,'user_permission':request.session['user_permission']})

            	if (len(new_pwd) < 8) or (len(new_pwd) > 25):
                	error = "Password must be atleast 8 characters long and max 25 characters"
                	return render_to_response('MyUser/edit_profile.html', {'error': error,'email':request.session['user_email'],'college':request.session['user_college'],'myuser':data,'user_permission':request.session['user_permission']})

            	error = ""

            	setattr(data, "user_password", new_pwd)
            	data.save()
            	request.session['error'] = new_pwd
            	return render_to_response('MyUser/edit_profile.html',{'success':"Password successfully updated",'email':request.session['user_email'],'college':request.session['user_college'],'myuser':data,'user_permission':request.session['user_permission']})
	
            else :  
                data = MyUser.objects.get(user_name=request.session['id'])            
                return render_to_response('MyUser/edit_profile.html',{'email':request.session['user_email'],'college':request.session['user_college'],'data':data,'user_permission':request.session['user_permission']})
        else : 
            return render_to_response('MyUser/login.html',{'success':"Enter the details"})

@csrf_exempt
def logout(request) :
    try :
        request.session['id'] = ""
        request.session['user_name'] = ""
        request.session['user_email'] = ""
        request.session['user_college'] = ""
        request.session['user_permission'] = ""
        request.session['error'] = ""   
        return HttpResponseRedirect('/login/')
    except :        
        return HttpResponseRedirect('/login/')

@csrf_exempt
def login(request) :
     
    try : 
        if request.session['id'] != "" : 
            return HttpResponseRedirect('/articles/all/')
        else : 
            if 'login' in request.POST : 
                data = MyUser.objects.get(user_name=request.POST['userName'],user_password=request.POST['userPassword'])
                request.session['id'] = getattr(data,"user_name")
                request.session['user_name'] = getattr(data,"user_name")
                request.session['user_email'] = getattr(data,"user_email")
                request.session['user_college'] = getattr(data,"user_college")
                request.session['number_posts'] = "5"
                request.session['user_permission'] = getattr(data,"user_permission") 
                return HttpResponseRedirect('/articles/all/')

            elif 'forgot' in request.POST:
            	data = MyUser.objects.get(user_name=request.POST['forgot_username'], user_email=request.POST['email'])
            	a = "" + str(random.randint(1, 10)) + str(random.randint(1, 10)) + str(random.randint(1, 10)) + str(random.randint(1, 10)) + str(getattr(data, "id")) + str(random.randint(1, 10)) + str(random.randint(1, 10)) + str(random.randint(1, 10)) + str(random.randint(1, 10))
            	hash_object = hashlib.sha256(b""+a)
            	a = hash_object.hexdigest()
            	setattr(data, "link", a)
            	request.session['forgot_user'] = request.POST['forgot_username']
            	data.save()
            	send_mail('Forgot Password', 'http://127.0.0.1:8000/forgot_passwd/'+a, 'emis.group1@gmail.com', [request.POST['email']])
            	return HttpResponseRedirect('/login/')

            else :
                return render_to_response('MyUser/login.html')
    except :
        request.session['id'] = ""
        return render_to_response('MyUser/login.html',{'error':"Wrong Username or Password"}) 

@csrf_exempt
def about(request):
	return render_to_response('MyUser/aboutpage.html')
        
@csrf_exempt
def forgot_password(request, offset):

	try : 	
		if request.POST:
					data = MyUser.objects.get(user_name=request.POST['userName'])
					setattr(data, "user_password", request.POST['for_new_password'])
					data.save()
					setattr(data, "link", "")
					data.save()
					request.session['id'] = getattr(data,"user_name")
					request.session['user_name'] = getattr(data,"user_name")
					request.session['user_email'] = getattr(data,"user_email")
					request.session['user_college'] = getattr(data,"user_college")
					request.session['number_posts'] = "5"
					return HttpResponseRedirect('/articles/all/')

	        else : 
			if(request.session['id'] == "") : 
				data = MyUser.objects.get(link = offset)
				a = getattr(data, "link")		
		       		return render_to_response("MyUser/for_chg_passwd.html", {'link':a, 'user_permission':request.session['user_permission'], 'show':True,'user_name':getattr(data,"user_name")})
			else : 
				return HttpResponseRedirect('/login/')	
       	except :	            	
   		return HttpResponseRedirect('/login/')


@csrf_exempt
def guest(request):
	request.session['id'] = "gue"
	request.session['user_permission'] = -1
	return HttpResponseRedirect('/articles/all/')

@csrf_exempt
def add_user(request):

	if request.session['id'] != "":
		if request.session['user_permission'] == 2 or request.session['user_permission'] == -1 : 				
		    return HttpResponseRedirect('/articles/all')

		if request.POST:
			userName = request.POST['username']
			password = request.POST['password']
			college = request.POST['college']
			email = request.POST['email']
			if 'optradio1' in request.POST:
				permission = 0
			elif 'optradio2' in request.POST:
				permission = 1
			elif 'optradio3' in request.POST:
				permission = 2
			user = MyUser(user_name=userName, user_password=password, user_college=college, user_email=email, user_permission=permission)
			user.save()
			if (len(password) < 8) or (len(password) > 25):
				error = "Password must be atleast 8 characters long and max 25 characters"
				return render_to_response('MyUser/addUser.html', {'error': error, 'user_permission':request.session['user_permission']})
				user.save()
				return HttpResponseRedirect('/articles/all/')
			else:
				return HttpResponseRedirect('/login/')
		else:
		    return render_to_response("MyUser/addUser.html", {'guest':True})
	else:
		return HttpResponseRedirect('/login/')  

@csrf_exempt
def myposts(request):

    try :
        if request.session['id'] != "" : 

            num = request.session['number_posts']            
            num = int(num)                     
            articles = Article.objects.filter(key = True, author = request.session['id'])    
            paginator = Paginator(articles,num)   
            page1 = paginator.page(1)
            author = request.session['id']
            return render_to_response("Article/list.html",{'posts' : page1,'author':author, 'num':num, 'user_permission':request.session['user_permission'], 'articles':False},context_instance=RequestContext(request))
        else :
            return HttpResponseRedirect('/login/')
    except :
        return HttpResponseRedirect('/login/')
