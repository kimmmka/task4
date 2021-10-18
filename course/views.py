from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from .models import Course
from .serializers import CourseSerializer

class CourseView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response({"courses": serializer.data})
    def post(self, request):
        course = request.data.get('course')
        serializer = CourseSerializer(data=course)
        if serializer.is_valid(raise_exception=True):
            course_saved = serializer.save()
        return Response({"success": "Course '{}' created successfully".format(course_saved.name)})
    
class CourseDetailView(APIView):
    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404
    def get(self, request):
        courses = self.get_object(pk)
        serializer = CourseSerializer(courses, many=True)
        return Response({"courses": serializer.data})
    def put(self, request, pk):
        saved_course = get_object_or_404(Course.objects.all(), pk=pk)
        data = request.data.get('course')
        serializer = CourseSerializer(instance=saved_course, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            course_saved = serializer.save()
        return Response({
            "success": "Course '{}' updated successfully".format(course_saved.name)})

    def delete(self, request, pk):
        # Get object with this pk
        course = get_object_or_404(Course.objects.all(), pk=pk)
        course.delete()
        return Response({
            "message": "Course with id `{}` has been deleted.".format(pk)
        }, status=204)