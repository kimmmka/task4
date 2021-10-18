from rest_framework import serializers


from .models import Course

class CourseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    description = serializers.CharField(max_length=120)
    category = serializers.CharField(max_length=120)
    logo = serializers.CharField(max_length=120)
    contacts = serializers.CharField(max_length=120)
    branches = serializers.CharField(max_length=120)

    def create(self, validated_data):
        return Course.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        instance.logo = validated_data.get('logo', instance.logo)
        instance.branches = validated_data.get('branches', instance.branches)
        instance.contacts = validated_data.get('contacts', instance.contacts)
        instance.save()
        return instance
        