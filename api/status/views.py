from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Status
from .serializers import StatusSerializer

class StatusListSearchAPIView(APIView):
    permission_classes = []
    authentication_classes = []
    
    def get(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)