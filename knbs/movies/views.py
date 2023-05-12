from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Movies
from django.shortcuts import render, redirect
from .serializers import MovieSerializer



@api_view(['POST'])
def api_movie(request):
    new_movie_data = request.data
    print(new_movie_data)

    # Verifique se o título e a nota estão presentes na requisição
    if 'title' in new_movie_data and 'nota' in new_movie_data:
        # Crie uma nova instância do modelo Movies
        movie = Movies(title=new_movie_data['title'], rating=new_movie_data['nota'])
        movie.save()

        # Serializar o objeto movie
        serialized_movie = MovieSerializer(movie)

        return Response(serialized_movie.data, status=200)
    else:
        return Response({'error': 'Dados incompletos'}, status=400)

# def extract_route(request):
#     if request == '':
#         return ''
#     return request.split(" ")[1][1:]



# def index(request):
#     if request.method == 'POST':
#         if request.path == '/nota':
#             title = request.POST.get('titulo')
#             nota = request.POST.get('nota')
#             # Cria um novo objeto Note com os dados recebidos pela requisição
#             Movies.objects.create(title=title, rating = nota)
#             return redirect('index')

#     else:
            
#             return render(request, 'olá')
    
# @api_view(['GET', 'POST'])
# def api_movie(request, movie_id):
    
#     try:
#         movie = Movies.objects.get(id = movie_id)
#     except Movies.DoesNotExist:
#         raise Http404()
#     if request.method == 'POST':
#         new_movie_data = request.data
#         movie.title = new_movie_data['title']
#         movie.rating = new_movie_data['rating']
#         movie.save()

#     serialized_movie = MovieSerializer(movie)
#     return Response(serialized_movie.data)