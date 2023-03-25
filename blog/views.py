from rest_framework import viewsets, permissions, status
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        instance.views += 1
        instance.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_permissions(self):
        if self.request.method == 'POST' or self.request.method == 'PUT' or self.request.method == 'DELETE':
            return [permissions.IsAdminUser()]
        else:
            return [permissions.AllowAny()]
