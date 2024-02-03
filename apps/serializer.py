# coding: utf-8

from rest_framework import serializers
from apps.models import Object


class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object

        # モデルに定義されているフィールドを全て指定
        fields = '__all__'
