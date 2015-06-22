import logging
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from Article.models import *
from django.http import HttpResponse
from forms import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.paginator import Paginator, InvalidPage ,EmptyPage
from django.core.urlresolvers import reverse
import hashlib
import random
from django.core.mail import send_mail

"""
Emagine - A Software Project undertaken by Group1 of CSE, Btech 2013 in IIT Patna.

"""


"""
1. *Edit Profile* :  User like Admin, Faculty and Student can edit their their profile. While editing
 a profile, change email address, Batch and their current password
2. *Login* : All Users who have valid usernames and password combination can login and do required 
    functions according to permissions.
3. *Logout* : All User can logout from site
"""    

@csrf_exempt
def create(request):
    try : 
        if request.session['id'] != "" :
            if request.session['user_permission'] == 2 or request.session['user_permission'] == -1 : 				
		        return HttpResponseRedirect('/articles/all/')
            if request.POST:

                title = request.POST.get('title');
                bdy =  request.POST.get('post');
                bdy = bdy.replace('\n', '<br/>')
                if 'tag' in request.POST:
                    tags = request.POST.get('tag');
                else:
                    tags = ""
                if 'file' in request.FILES:
                    docfile = request.FILES.get('file');
                else:
                    docfile = None
                auth = request.session['id'];
                data = Article(title=title, body=bdy, tag=tags, author=auth, doc=docfile)                          
                setattr(data, "key", True)
                data.save()
                return HttpResponseRedirect('all/') 
        
            else : 
                return render_to_response('Article/create_article.html', {'user_permission':request.session['user_permission']})
        else : 
            return HttpResponseRedirect('/login/')
    except : 
        return HttpResponseRedirect('/login/')                         

@csrf_exempt
def main(request):

    try :
        if request.session['id'] != "" : 

            num = request.session['number_posts']            
            num = int(num)
            articles = Article.objects.filter(key = True).order_by('-date')    
            paginator = Paginator(articles,num) 
            array = []
            for a in range(1,paginator.num_pages):
            	array.append(a)
            current = 1 
            page1 = paginator.page(1)
            author = request.session['id']
            return render_to_response("Article/list.html",{'user_name':request.session['user_name'],'array':array, 'current':current, 'posts' : page1,'author':author, 'num':num, 'user_permission':request.session['user_permission'], 'articles':True},context_instance=RequestContext(request))
        else :
            return HttpResponseRedirect('/login/')
    except :
        return HttpResponseRedirect('/login/')

@csrf_exempt    
def main_offset(request, offset):                              #direct to requested page from offset
    
    try :
        if request.session['id'] != "" :            
            author = request.session['id']
            articles = Article.objects.filter(key = True).order_by('-date')
            num = request.session['number_posts']
            num = int(num)
            number = int(offset)
            paginator = Paginator(articles,num)
            if number <= paginator.num_pages :                          #if number is valid (less than maximum pages in paginator)
                page1 = paginator.page(number)
                num1 = page1.__len__()
                array = []
            	for a in range(1,paginator.num_pages):
            		array.append(a)
            	current = number 
            else : 
                page1 = paginator.page(1)                        #direct user to first page
                array = []
            	for a in range(1,paginator.num_pages):
            		array.append(a)
            	current = 1 
            
            return render_to_response("Article/list.html",{'user_name':request.session['user_name'],'array':array, 'current':current, 'posts' : page1,'author':author, 'user_permission':request.session['user_permission'], 'num':num, 'num1':num1, 'articles':True})
        else :
            return HttpResponseRedirect('/login/')
    except : 
        return HttpResponseRedirect('/login/')

@csrf_exempt
def load_article(request,offset) :                                                                 #here offset marks the id of article

        if request.session['id'] != "" :
            form = CommentsForm()
            args = {}
            args.update(csrf(request))

            if 'like' in request.POST :                                                                #person has clicked on 'like'                 
                _offset = int(offset)
                current_page = Article.objects.get(id = _offset)                
                setattr(current_page,"likes",getattr(current_page,"likes")+1)
                setattr(current_page,"like_articles",getattr(current_page,"like_articles")+offset)
                current_page.save()                               
                comment_list = []
                comment_list = Comments.objects.filter(parent_article_id = offset)                        
                return HttpResponseRedirect('/load/'+offset)
            
            elif 'unlike' in request.POST :
            	_offset = int(offset)
                current_page = Article.objects.get(id = _offset)                
                setattr(current_page,"likes",getattr(current_page,"likes")-1)
                setattr(current_page,"like_articles",getattr(current_page,"like_articles").replace(str(offset),"0"))
                current_page.save()                               
                comment_list = []
                comment_list = Comments.objects.filter(parent_article_id = offset)                        
                return HttpResponseRedirect('/load/'+offset)

            elif 'comments' in request.POST :
            	if request.POST:
	                bdy =  request.POST.get('comments');
	                auth = request.session['id'];
	                data = Comments(comment=bdy, author=auth, parent_article_id=offset)
	                data.save()                      
	                current_page = Article.objects.get(id = offset)
	                setattr(current_page, "num_comm", getattr(current_page, "num_comm")+1)
	                current_page.save()
	                return HttpResponseRedirect('/load/'+offset)

            elif 'delete' in request.POST:
                current_page = Article.objects.get(id = offset)
                author = current_page.author
                
                if request.session['id'] == author :
                    setattr(current_page, "key", False)
                    current_page.save()
                    return HttpResponseRedirect('/articles/all')

                else :
                    return HttpResponseRedirect('/load/'+offset)

            elif 'edit' in request.POST:

                current_page = Article.objects.get(id = offset)
                author = getattr(current_page, "author")

                if author == request.session['id']:
                    body = getattr(current_page, "body")
                    key = True
                    offset = int(offset)                
                    current_page = Article.objects.get(id = offset)
                    comment_list = []
                    comment_list = Comments.objects.filter(parent_article_id = offset)    
                    return render_to_response("Article/display_article.html", {'post':current_page,'form':form,'comments':comment_list, 'key':key, 'key1':True, 'user_permission':request.session['user_permission']}, context_instance=RequestContext(request))

                else:
                    return HttpResponseRedirect('/load/'+offset)

            elif 'edit_post' in request.POST:

                current_page = Article.objects.get(id = offset)
                author = getattr(current_page, "author")

                if author == request.session['id']:
                    setattr(current_page, "body", request.POST['edit_post'])
                    current_page.save()
                    comment_list = []
                    comment_list = Comments.objects.filter(parent_article_id = offset)
                    return render_to_response("Article/display_article.html", {'post':current_page,'form':form,'comments':comment_list, 'key':False, 'key1':True, 'user_permission':request.session['user_permission']}, context_instance=RequestContext(request))

            else :
            	off = offset
                offset = int(offset)
                current_page = Article.objects.get(id = offset)
                comment_list = []
                comment_list = Comments.objects.filter(parent_article_id = offset)
                num_comm = getattr(current_page, "num_comm")
                likes = getattr(current_page, "likes")
                if request.session['user_permission'] >= 0:
	                data = MyUser.objects.get(user_name = request.session['user_name'])
                liked_Articles = getattr(current_page, "like_articles")
                if liked_Articles.find(str(offset)) == -1 : 
                	like = "like"
                else :
                	like = "unlike"		
                if request.session['id'] == getattr(current_page, "author") :
                    key1 = True
                else:
                    key1 = False
                return render_to_response("Article/display_article.html",{'likes':likes, 'num_comm':num_comm, 'like':like,'post':current_page,'form':form,'comments':comment_list, 'key':False, 'key1':key1, 'user_permission':request.session['user_permission']}, context_instance=RequestContext(request))

        else :
            return HttpResponseRedirect('/login/')

@csrf_exempt
def search_titles(request):
	if request.method == "POST":
		search_text = request.POST['search_text']
	else:
		search_text = 'zzzzzzzzzzzzz'
	if search_text == "":
		search_text = 'zzzzzzzzzzzzz'
	else:
		args = {}
		args.update(csrf(request))
		articles = Article.objects.filter(title__icontains=search_text, key=True).order_by('title') | Article.objects.filter(tag__icontains=search_text, key=True)| Article.objects.filter(author__icontains=request.session['user_name'], key=True)
		return render_to_response('Article/ajax_search.html', {'articles':articles, 'user_permission':request.session['user_permission']})

@csrf_exempt    
def load_page(request, offset):                              #direct to requested page from offset
    
    #offset = int(offset)   
    request.session['number_posts'] = offset
    num = request.session['number_posts']
    return HttpResponseRedirect('/articles/all/')

"""
def load_page1(request, offset):
 	request.session['sort'] = offset

 	if offset == "like":
 		data = Article.objects.filter(key = True).order_by('-likes')
 	elif offset == "day":
 		data = Article.objects.filter(key = True).order_by('date').
"""
@csrf_exempt    
def page_offset(request, offset):                              #direct to requested page from offset
    
    try :
        if request.session['id'] != "" :            
            author = request.session['id']
            articles = Article.objects.filter(key = True, author = request.session['id'])
            num = request.session['number_posts']
            num = int(num)
            number = int(offset)
            paginator = Paginator(articles,num)
            if number <= paginator.num_pages :                          #if number is valid (less than maximum pages in paginator)
                page1 = paginator.page(number)
                num1 = page1.__len__()
            else : 
                page1 = paginator.page(1)                         #direct user to first page
            
            return render_to_response("Article/list.html",{'user_name':request.session['user_name'],'posts' : page1,'author':author, 'user_permission':request.session['user_permission'], 'num':num, 'num1':num1, 'articles':False})
        else :
            return HttpResponseRedirect('/login/')
    except : 
        return HttpResponseRedirect('/login/')
