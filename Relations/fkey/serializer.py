from rest_framework import serializers
from  .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = Author
#end class
"""
class BookSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(write_only=True)
    name = serializers.CharField(max_length=50)
    author = AuthorSerializer(read_only = False)

    class Meta:
        model = Book
        fields = ('id', 'name', 'author', 'author_id',)
"""

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Book
        