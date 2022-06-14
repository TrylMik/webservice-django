from msilib.schema import ListBox
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import *
from .forms import *

# Create your views here.

def index(response):
    return render(response, "main/base.html", {})

def home(response):
    return render(response, "main/home.html", {})

def questions(response):
    return render(response, "main/questions.html", {})

def movies(response):
    return render(response, "main/movies.html", {})

def photos(response):
    return render(response, "main/photos.html", {})

class Spots(ListView):
    model = SpotsPost
    template_name = 'main/spots.html'

class SpotsDetails(DetailView):
    model = SpotsPost
    template_name = 'main/spots_post_detail.html'

class AddSpots(CreateView):
    model = SpotsPost
    form_class = PostSpotForm
    template_name = 'main/create_spots.html'
    #fields = ('title', 'body')

class AddCommentSpots(CreateView):
    model = SpotsComment
    form_class = CommentSpotForm
    template_name = 'main/comment_spots.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('Spots')

class DeleteSpot(DeleteView):
    model = SpotsPost
    template_name = 'main/delete_spots.html'
    success_url = reverse_lazy('Spots')
