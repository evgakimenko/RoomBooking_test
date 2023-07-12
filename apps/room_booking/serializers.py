from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Room, Reservation


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'room', 'price', 'capacity')


class ReservationSerializer(serializers.ModelSerializer):
    room = serializers.StringRelatedField()
    user = serializers.StringRelatedField()

    class Meta:
        model = Reservation
        fields = ('id', 'room', 'user', 'check_in', 'check_out')

    def create(self, validated_data):
        # Create a new reservation
        reservation = Reservation.objects.create(**validated_data)
        return reservation


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        # Create a new user
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user
