from rest_framework import generics

from api.models import Person, Movie
from api.serializers import PersonSerializer, MovieSerializer


class PersonListView(generics.ListCreateAPIView):
    # queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()


class PersonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
