from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import TeacherView , StudentView

router= DefaultRouter()

router.register (r'teachers' , TeacherView)
router.register (r'students' , StudentView)
urlpatterns = [

    path('api/' , include (router.urls)),
]