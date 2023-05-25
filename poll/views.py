from django.http import HttpResponse
from django.shortcuts import render, redirect,get_list_or_404
from .forms import CreatePollForm
from .models import *

def home(request):
    polls = Poll.objects.all()
    
    context = {
        'polls': polls
    }
    return render(request, 'Poll/home.html', context)
def createnow(request):
    if request.method == 'POST':
        question = request.POST['question']
        option_one = request.POST['option_one']
        option_two = request.POST['option_two']
        option_three = request.POST['option_three']

        newform = Poll(question = question,option_one = option_one,option_two = option_two,option_three = option_three)
        newform.save()

        return redirect('home')
    
    return render(request,'Poll/create.html')
def result(request):
    user_option =   objectsave.objects.all()
    option_one  = objectsave.objects.filter(option = "option1")
    option_two = objectsave.objects.filter(option = "option2")
    option_three = objectsave.objects.filter(option = "option3")

    optionval_one = option_one.count()
    optionval_two = option_two.count()
    optionval_three = option_three.count()

    total = optionval_one + optionval_two + optionval_three
    

    

    context = {
        'option_one_count':optionval_one,
        'option_two_count':optionval_two,
        'option_three_count':optionval_three,
        "total":total

    }
    return render(request,'Poll/results.html',context)

#def results(request):
    #poll = Poll.objects.filter(pk = Poll.poll_id)
        
    #context = {
     #   'poll': poll
    #}
    #return render(request, 'Poll/results.html', context)

def vote(request):
    vote = Poll.objects.all()
    if request.method == 'POST':
        option = request.POST['option']
        options = objectsave(option=option)
        options.save()
        context = {
            'poll':options
        }
        return redirect('result')
   
    context = {
       "votes":vote
    }
    return render(request, 'Poll/vote.html',context)

