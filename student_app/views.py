from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class AllStudents(APIView):

    def get(self, request):
        all_students = Student.objects.all()
        serialized_all_students = StudentSerializer(all_students, many=True)
        return Response(serialized_all_students.data)