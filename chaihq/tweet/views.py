from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

def index(request):
  return render(request,'index.html')

@login_required #this decorator wraps the entire function in the login functionality
def createTweet(request):
  if request.method == 'POST':
    form = TweetForm(request.POST, request.FILES)
    if form.is_valid():
      tweet = form.save(commit=False) #commit=false means abhi db mein store nahi krna chahta
      tweet.user = request.user
      tweet.save()
      return redirect('tweet_list')
  else:
    # empty form
    form = TweetForm()
  return render(request, 'tweet_form.html', {'form':form})

def listTweets(request):
  tweets = Tweet.objects.all().order_by('-created_at')
  return render(request, 'tweet_list.html', {'tweets': tweets})

@login_required
def editTweet(request, tweet_id):
  tweet = get_object_or_404(Tweet, pk=tweet_id, user= request.user)
  if request.method == 'POST':
    form = TweetForm(request.POST, request.FILES, instance=tweet)
    if form.is_valid():
      update = form.save(commit=False)
      update.user = request.user
      update.save()
      return redirect('tweet_list')
  else:
    # instance added because we want to showcase prefilled form as we are updating our tweet
    form = TweetForm(instance=tweet)
  return render(request, 'tweet_form.html', {'form':form})

@login_required
def deleteTweet(request, tweet_id):
  tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
  if request.method == 'POST':
    tweet.delete()
    return redirect('tweet_list')
  return render(request, 'tweet_confirm_delete.html', {'tweet':tweet})

def register(request):
  if(request.method == 'POST'):
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      # cleaned_data inbuilt function - used jab bhi form k andar se data uthaana ho
      # set_password - also inbuilt function
      user.set_password(form.cleaned_data['password1'])
      user.save()
      # automatically login after registration
      login(request, user)
      return redirect('tweet_list')
  else:
    form = UserRegistrationForm()
  return render(request, 'registration/register.html', {'form':form})

# def login(request):
#   user =
#   return render(request, login(request,user))