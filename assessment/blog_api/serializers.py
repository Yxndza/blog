from rest_framework import serializers
from .models import Post, Contact

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "content", "author", "published_date"]


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["name", "email", "phone", "message"]
        