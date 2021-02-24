from django.shortcuts import render,redirect
from .models import review
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
def review_list (request) : 
    reviews = review.objects.all().order_by('date') #error faltu mien arha ha
    return render(request, 'reviews/review_list.html', {'reviews':reviews})


def review_detail(request, slug): 
    # return HttpResponse(slug)
    review_det = review.objects.get(slug=slug)
    return render(request, 'reviews/review_detail.html', {'review':review_det})



@login_required(login_url = "/accounts/login/") #protecting this user to login will first check if the user is logged in or not
def review_create(request) : 
    if request.method == 'POST':
        form = forms.Createreview(request.POST, request.FILES)
        if form.is_valid():
            #saving the review to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('reviews:list')
    else:
        form = forms.Createreview()
    return render(request, 'reviews/review_create.html', {'form':form})