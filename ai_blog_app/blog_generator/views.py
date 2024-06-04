from django.shortcuts import render
#You will import user, authenticate, login and logout, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
'''in order to buid a dashboard whereby you dont want anyone that doesnt login t access it import a decorator, then goto the settings.py to declear this variable at the bottom LOGIN_URL = 'login'
'''
from django.contrib.auth.decorators import login_required
'''
in order exempt csrf_token in or blog generator we will need to import it but you need not to exempt it when you are doing real life project
'''
from django.views.decorators.csrf import csrf_exempt
#in order to use a json response, you will need to import it
from django.http import JsonResponse
import json
#you will need to install pytube with pip. use pip install pytube
from pytube import Youtube
from django.conf import settings
import os
#you will also need to install assemblyai. use pip install assemblyai
import assemblyai as aai
#you will also need to install assemblyai. use pip install openai
import openai
# Create your views here.
from .models import BlogPost #this is where you import your database
@login_required
def index(request):
    return render(request, 'index.html')
    
@csrf_exempt
def generate_blog(request):
    if request.method == 'POST':
        try:
            data = json.load(request.body)
            yt_link = data['link']
            
        except (KeyError, json.JSONDecodeError):
            return JsonResponse({'error': 'Invalid request method'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    #get yt title
     title = yt_title(yt_link)
    #get transcript
     transcription = get_transcription(yt_link)
        if not transcription:
           return JsonResponse({'error': 'Failed to get transcript'}, status=500) 
    #use OpenAI to generate the blog
    blog_content = generated_blog_fro_transcription(transription)
    if not blog_content:
        return JsonResponse({'error': 'Failed to generate blog article'}, status=500) 
    #save blog article to database
     new_blog_article = BlogPost.object.create{
     user=request.user,
     youtube_title=title,
     youtube_link=yt_link,
     generated_content=blog_content,
     }
     new_blog_article.save()
    #returnblog article as a response
    return JsonResponse({'content': blog_content})
def  yt_title(link):
        yt = Youtube(link)
        title = yt.title
    return title
def download_audio(link):
    yt = YouTube(link)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=settings.MEDIAL_ROOT)
    base, ext = os.path.splitext(out_file)
    new_file = base+ '.mp3'
    os.rename(out_file, new_file)
    return new_file

def get_trascription(link):
    audio_file = download_audion(link)
    aai.settings.api_key = "867f9d5714ff48df8dc6f7e926c9b792"
    
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(audio_file)
    
    return transcribt.text
def generate_blog_from_transcription(transcription):
    openai.api_key = "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"
    
    prompt = f"Based on the following transript from a YouTube video, write a comprehensive blog article, write it based on the transcript, but dont make it look like a youtube video, make it look like a proper blog article:\n\n{transcription}\n\nArticle:"
    response = openai.Completion.create{
    model="text-devinci-003"
    max_tokens=1000
    }
    
    generated_content = response.choice[0].text.strip()
    return generated_content
def blog_list(request):
    blog_articles = BlogPost.objects.filter(user=request.user)
    return render(request, "all-blogs.html",{'blog_articles': blog_articles})
def blog_details(request, pk):
    blog_article_detail = BlogPost.objects.get(id=pk)
    if request.user == blog_article_detail.user
        return render(request, 'blog-details.html', {'blog_article_detail': blog_article_detail})
    else
        return redirect('/')
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message':error_message})
            
    return render(request, 'login.html')
    
def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeatpassword = request.POST['repeatpassword'] 
        
        if password == repeatpassword:
            try:
                user = User.object.create_user(username, email, password)
                user.save()
                login(request, user)
                return redirect('/')
            except:
                error_message = 'Password do not match'
                return render(request, 'signup.html', {'error_message':error_message})    
        else:
            error_message = 'Password do not match'
            return render(request, 'signup.html', {'error_message':error_message})
    return render(request, 'signup.html')
    
def user_logout(request):
    logout(request)
    return redirect('/')
