from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('',views.StudentListCreateAPIView.as_view()),
    path('user/register/',views.CeateUserView.as_view(),name="register"),
    path('token/',TokenObtainPairView.as_view(),name="get_token"),
    path('token/refresh',TokenRefreshView.as_view(),name="refresh"),
    path('testapi-auth/',include("rest_framework.urls")),

    path('notes/',views.NoteListCreateView.as_view(),name='note_list_create'),
    path('notes/delete/<int:pk>/',views.NoteDelete.as_view(),name="note_delete")
]