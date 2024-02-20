import json
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import NoteSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Notes, NotesHistory
from datetime import datetime

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateNoteView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = NoteSerializer
    queryset = Notes.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        note_obj = Notes.objects.get(id = serializer.data.get("id"))
        NotesHistory.objects.create(
            note = note_obj,
            history_detail = json.dumps({"Created":[{
                "date":str(datetime.now())
            }]}
        ))


class NoteRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Notes.objects.all()

    def get(self, request, *args, **kwargs):
        return self.get_object()

    def put(self, request, *args, **kwargs):
        note = Notes.objects.get(id = kwargs.get("pk"))
        if self.request.user == note.created_by:
            return self.update(request, *args, **kwargs)
        else:
            return Response({"message": "You do not have access to edit this note"})


class GetNoteHistoryView(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        note_history = NotesHistory.objects.get(note = kwargs.get("id")).history_detail
        return Response(json.loads(note_history), status=status.HTTP_200_OK)