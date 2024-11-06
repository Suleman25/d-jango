from django.urls import path
from secondapp import views
from .views import index
urlpatterns = [
    # path('jan/' , views.jan),
    # path('feb/' , views.feb),
    # path('mar/' , views.mar),
    # path('apr/' , views.apr),
    # path('may/' , views.may),
    # path('jun/' , views.jun),
    # path('jul/' , views.jul),
    # path('aug/' , views.aug),
    # path('sep/' , views.sep),
    # path('oct/' , views.oct),
    # path('nov/' , views.nov),
    # path('dec/' , views.dec),
    # path('<str:months>/',index.as_view()),
     path('jan/', index.as_view()),
]