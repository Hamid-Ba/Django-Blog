from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions

from ... import models

class RegisterSerializer(serializers.ModelSerializer):
    """Register Serializer"""
    password1 = serializers.CharField(max_length=225,write_only=True)
    class Meta:
        model = models.User
        fields = ['email','password','password1']

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password1') :
            raise serializers.ValidationError("Password Doesn't Match")
        
        try :
            validate_password(attrs.get('password'))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError(list(e.messages))

        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop('password1', None)
        return super().create(validated_data)

class ChangePasswordSerializer(serializers.Serializer):
    """Change Password Serializer"""
    old_password = serializers.CharField(max_length=225,write_only=True)
    password = serializers.CharField(max_length=225,write_only=True)
    password1 = serializers.CharField(max_length=225,write_only=True)

    def validate(self, attrs):
        user = self.context['request'].user
        new_password = attrs.get('password')
        
        if not user.check_password(attrs.get('old_password')) : raise serializers.ValidationError("Password Is Wrong!")
        if attrs.get('password') != attrs.get('password1') : raise serializers.ValidationError("Password Doesn't Match")

        user.set_password(new_password)
        user.save()

        return super().validate(attrs)

class ProfileSerializer(serializers.ModelSerializer):
    """Profile Serializer"""
    email = serializers.EmailField(source = 'user.email',read_only=True)
    # avatar = serializers.ImageField()
    class Meta:
        model = models.Profile
        fields = '__all__'
        read_only_fields = ['id','user','email','created_data','updated_data']