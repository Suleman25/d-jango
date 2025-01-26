from django.urls import path
from thirdapp import views

urlpatterns=[
    path('allbooks/',views.bookView.as_view(),name='book-list'),
    path('enter-book/',views.createView.as_view(),name='list'),
    path('retrieve/<int:id>/',views.retrieveView.as_view(),name='one'),
    path('delete/<int:id>/',views.deleteView.as_view(),name='delete'),
    path('students/',views.studentView.as_view(),name='list')
]