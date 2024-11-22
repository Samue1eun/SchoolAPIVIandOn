
from .models import Subject
from .serializers import SubjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class AllSubjects(APIView):

    def get(self, request):
        all_subjects = Subject.objects.all()
        serialized_all_subjects = SubjectSerializer(all_subjects, many=True)
        return Response(serialized_all_subjects.data)