from sites.models import Site
from sites.serializers import SiteSerializer
from django.contrib.auth.models import User
from sites.serializers import UserSerializer
from rest_framework import permissions
from sites.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets

class UserViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class SiteViewSet(viewsets.ModelViewSet):
	queryset = Site.objects.all()
	serializer_class = SiteSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)



