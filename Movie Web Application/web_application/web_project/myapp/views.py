from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Movie
from .forms import AddMovies


# Create your views here.

def index(request):
    movie = Movie.objects.all()
    context = {'movie_list': movie}
    return render(request, 'index.html', context)


def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'details.html', {'movie': movie})


def login(request):
    return render(request, 'login.html')


def sign(request):
    return render(request, 'sign.html')


def add_movies(request):
    if request.method == "POST":
        form = AddMovies(request.POST or None, request.FILES)
        movie = Movie(form)
        if form.is_valid():
            movie.save()
    form = AddMovies()
    dict_form = {'form': form}

    return render(request, 'add.html', dict_form)


def update(request, id):
    movie = Movie.objects.get(id=id)
    form = AddMovies(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return render(request, 'confirmation.html')

    return render(request, 'update.html', {'form': form, 'movie': movie})


def movies(request):
    dict_movies = {'movies': Movie.objects.all()}
    return render(request, 'movies.html', dict_movies)


def profiles(request):
    email = "jeminmthw997@gmail.com"
    return HttpResponseRedirect("https://www.gmail.com")

def delete(request,id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')

def user(request):
    return render(request,'user.html')