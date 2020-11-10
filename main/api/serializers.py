from rest_framework import serializers
from main.models import Bitcoin


class BitcoinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bitcoin
        fields = ('price', 'last_updated', 'created')
