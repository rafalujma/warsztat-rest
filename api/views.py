from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from api.models import Person, Movie
from api.serializers import PersonSerializer, MovieSerializer, LoginSerializer


class PersonListView(generics.ListCreateAPIView):
    # queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Person.objects.all()


class PersonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"user_id": user.id, "token": token.key})

        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
