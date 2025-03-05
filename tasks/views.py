from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer


class CategoryListCreateAPIView(APIView):
    """Отримання списку категорій або створення нової"""

    @swagger_auto_schema(
        operation_summary="Отримати список всіх категорій",
        responses={200: CategorySerializer(many=True)}
    )
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Створити нову категорію",
        request_body=CategorySerializer,
        responses={201: CategorySerializer(), 400: "Invalid data"}
    )
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailAPIView(APIView):
    """Отримання, оновлення та видалення категорії"""

    @swagger_auto_schema(
        operation_summary="Отримати категорію за ID",
        responses={200: CategorySerializer(), 404: "Not found"}
    )
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Оновити категорію за ID",
        request_body=CategorySerializer,
        responses={200: CategorySerializer(), 400: "Invalid data", 404: "Not found"}
    )
    def put(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Видалити категорію за ID",
        responses={204: "Deleted", 404: "Not found"}
    )
    def delete(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response({"message": "Category deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class TaskListCreateAPIView(APIView):
    """Отримання списку завдань або створення нового"""

    @swagger_auto_schema(
        operation_summary="Отримати список всіх завдань",
        responses={200: TaskSerializer(many=True)}
    )
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Створити нове завдання",
        request_body=TaskSerializer,
        responses={201: TaskSerializer(), 400: "Invalid data"}
    )
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailAPIView(APIView):
    """Отримання, оновлення та видалення завдання"""

    @swagger_auto_schema(
        operation_summary="Отримати завдання за ID",
        responses={200: TaskSerializer(), 404: "Not found"}
    )
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Оновити завдання за ID",
        request_body=TaskSerializer,
        responses={200: TaskSerializer(), 400: "Invalid data", 404: "Not found"}
    )
    def put(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Видалити завдання за ID",
        responses={204: "Deleted", 404: "Not found"}
    )
    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return Response({"message": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)