from rest_framework import generics, pagination, permissions, status, response
from django.http import JsonResponse
from django.db.models import Q
from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer, SimplePostSerializer
from rest_framework.views import APIView

class PostPagination(pagination.PageNumberPagination):
    page_size = 4

    def get_paginated_response(self, data):
        return response.Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'results': data,
            'page_size': self.page_size,
            'range_first': (self.page.number * self.page_size) - (self.page_size) + 1,
            'range_last': min((self.page.number * self.page_size), self.page.paginator.count),
        })

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = SimplePostSerializer
    pagination_class = PostPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.query_params.get('keyword', None)
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(lead_text__icontains=keyword)
            )

        category = self.request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(category=category)
        print(queryset)
        return queryset

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