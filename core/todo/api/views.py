from .serializers import TaskSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ..models import Task
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .paginations import LargeResultsSetPagination
from .permissions import IsOwnerOrReadOnly

class TodoListView(viewsets.ModelViewSet):
     permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
     serializer_class = TaskSerializer
     queryset = Task.objects.all()
     filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
     filterset_fields = ['complete']
     search_fields = ['title']
     ordering_fields = ['created_date']
     pagination_class = LargeResultsSetPagination
# class TodoDetailApiView(viewsets.ModelViewSet):
#      permission_classes = [IsAuthenticatedOrReadOnly]
#      serializer_class = TaskSerializer
#      queryset = Task.objects.all()

