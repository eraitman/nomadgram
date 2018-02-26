from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers


class ListAllImages(APIView):

    def get(self, request, format=None):
        all_image = models.Image.objects.all()
        serializer = serializers.ImageSerializer(all_image, many=True)
        print(repr(serializer.data))
        return Response(data=serializer.data)