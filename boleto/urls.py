from django.conf.urls.defaults import *
from djboleto.boleto.views import imagem_barras

urlpatterns = patterns('',
    url(r'imagem_barras/$', imagem_barras, name='imagem_barras')
)
