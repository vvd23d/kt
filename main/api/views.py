from rest_framework.generics import ListAPIView
from main.models import Bitcoin
from .serializers import BitcoinSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions


class BitcoinListView(ListAPIView):
    queryset = Bitcoin.objects.all()
    serializer_class = BitcoinSerializer
    permission_classes = (permissions.AllowAny, )


class LastBtcAPIView(APIView):
    def get(self, request):
        btc = Bitcoin.objects.last()
        serializer = BitcoinSerializer(btc)
        return Response(serializer.data)





"""class TelAPIView(APIView):

    def get(self, request, tel):
        message = None

        if tel.isdigit():
            if tel.startswith('79'):
                if len(tel) == 11:
                    search_kod = tel[1:4]
                    search_nom = tel[4:11]

                    tels = Numbering.objects.filter(Q(kod__icontains=search_kod) &
                                                    Q(fr__lt=int(search_nom)) &
                                                    Q(to__gt=int(search_nom)))

                    serializer = NumberingSerializer(tels[0])
                else:
                    message = "Номер телефона должен иметь длину 11 символов!"
            else:
                message = "Номер телефона должен начинаться на символы '79'!"
        else:
            message = "В номере телефона не должно быть никаких других символов, кроме цифр!"
        if message:
            return Response(json.loads('{"Error":"' + message + '"}'))
        else:
            return Response(serializer.data)"""

