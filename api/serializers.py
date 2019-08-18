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
