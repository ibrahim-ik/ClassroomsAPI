from rest_framework import serializers
from classes.models import Classroom
from django.contrib.auth.models import User



class UserListSerializer(serializers.ModelSerializer):

	teacher = serializers.SerializerMethodField()

	detail = serializers.HyperlinkedIdentityField(
        view_name = "api-detail",
        lookup_field = "id",
        lookup_url_kwarg = "classroom_id"
        )

	class Meta:
		model = Classroom
		fields = [
		'subject',
		 'year',
		 'teacher',
		 'detail',
		 ]


	def get_teacher(self, obj):
		return obj.teacher.username


class UserDetailSerializer(serializers.ModelSerializer):

	teacher = serializers.SerializerMethodField()

	update = serializers.HyperlinkedIdentityField(
        view_name = "api-update",
        lookup_field = "id",
        lookup_url_kwarg = "classroom_id"
        )

	delete = serializers.HyperlinkedIdentityField(
        view_name = "api-delete",
        lookup_field = "id",
        lookup_url_kwarg = "classroom_id"
        )

	class Meta:
		model = Classroom
		fields = [
		'name',
		'subject',
		 'year',
		 'teacher',
		 'update',
		 'delete',
		 ]


	def get_teacher(self, obj):
		return obj.teacher.username



class UserCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Classroom
		exclude =['teacher']



class UserUpdateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Classroom
		fields = [
		'name',
		'subject',
		 'year',
		 ]

