from rest_framework import serializers
from sites.models import Site

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	sites = serializers.HyperlinkedRelatedField(many=True, view_name='site-detail', read_only=True)
	class Meta:
		model = User
		fields = ('url','id', 'username', 'sites')

class SiteSerializer(serializers.HyperlinkedModelSerializer):	
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Site
		fields = ('url', 'id', 'owner','site', 'criteria', 'in_danger', 'http_url', 'image_url','iso_code',
			'latitude','longitude','region','short_description','states','transboundary','unique_number','year',
			'cultural','natural','mixed','delisted')
