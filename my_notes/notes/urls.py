from django.urls import path
from .views import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('notes/create/',CreateNoteView.as_view(),name='create_note'),
    path('notes/<str:pk>/',NoteRetrieveUpdateView.as_view(),name='retrieve_update_notes'),
    path('note/version-history/<str:id>/',GetNoteHistoryView.as_view(),name='version-history')
]
