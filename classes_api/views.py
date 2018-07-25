from classes.models import Classroom
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	DestroyAPIView,
	CreateAPIView,
)
from .serializers import (
	UserListSerializer,
	UserDetailSerializer,
	UserCreateSerializer,
	UserUpdateSerializer,
)



class ClassroomListView(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = UserListSerializer
	permission_classes = [AllowAny,]


class ClassroomDetailView(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = UserDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'
	permission_classes = [AllowAny,]



class ClassroomCreatelView(CreateAPIView):
	 queryset = Classroom.objects.all()
	 serializer_class = UserCreateSerializer

	 def perform_create(self, serializer):
		 serializer.save(teacher=self.request.user)


class ClassroomUpdateView(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = UserUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'


class ClassroomDeleteView(DestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = UserListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'



# Create your views here.
