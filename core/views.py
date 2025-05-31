"""API Start"""

from rest_framework.views import APIView
from rest_framework.response import Response


class TestView(APIView):
    """Response"""

    def get(self, request, *args, **kwargs):
        """Response"""
        return Response("Hello World!")
