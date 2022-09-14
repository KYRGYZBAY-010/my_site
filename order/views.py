from email.mime import image
from http.client import IM_USED
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django.shortcuts import render
from notifiers import get_notifier
from .serializers import ImSerializers, ProjectSerializers, BotSerializer
from .models import I_m, Projects
from .bot import token, my_id



def index(request):
    im_dict = {}
    projects = []
    pro = Projects.objects.all()
    projects.append(pro)
    im = I_m.objects.all()
    im_dict['i_m'] = im
    im_dict['projects'] = projects
    return render(request, 'main/content.html', {'im_dict': im_dict})




class ImView(GenericAPIView):
    serializer_class = ImSerializers


    def get(self, request):
        pass


class BotView(GenericAPIView):
    serializer_class = BotSerializer

    def post(self, request):
        serializer = BotSerializer(request.data)
        name = serializer.data['name']
        phone = serializer.data['phone']
        company = serializer.data['name_company']
        email = serializer.data['email']
        message = "Заявка!" '\n' + "Имя: " + str(name) +'\n' "Номер телефона: " + str(phone) + '\n' "Имя компании: " + str(company) + '\n' "E-mail: "+ str(email)
        telegram = get_notifier('telegram')
        telegram.notify(token = token, chat_id = my_id, message = message)
        return Response('ok')

