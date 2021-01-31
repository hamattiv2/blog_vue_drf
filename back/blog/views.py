from rest_framework import generics, status, permissions
from django.http import JsonResponse
from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer, SimplePostSerializer
from rest_framework.views import APIView

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = SimplePostSerializer

class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class GetTestAPI(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        response = JsonResponse(
            {
                'data': {'status': 'hello'},
                'status': status.HTTP_200_OK
            }
        )
        return response