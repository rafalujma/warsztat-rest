from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Person, Movie


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["id", "first_name", "last_name"]


class MovieSerializer(serializers.ModelSerializer):
    directed_by = PersonSerializer(read_only=True)
    directed_by_id = serializers.PrimaryKeyRelatedField(
        source="directed_by", queryset=Person.objects.all(), write_only=True
    )

    class Meta:
        model = Movie
        fields = ["id", "title", "launched_on", "directed_by", "directed_by_id"]


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        try:
            user = User.objects.get(username=data["username"])
        except User.DoesNotExist:
            raise serializers.ValidationError("Błąd logowania!")

        if not user.check_password(data["password"]):
            raise serializers.ValidationError("Błąd logowania!")
        return {"user": user}

