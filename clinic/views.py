from rest_framework import viewsets, exceptions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from .models import Owner, Pet, MedicalRecord
from .serializers import OwnerSerializer, PetSerializer, MedicalRecordSerializer


class OwnerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['name', 'phone']
    ordering = ['id']


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    filterset_fields = ['species', 'birth_year', 'owner']

    search_fields = ['name', 'owner__name', 'species']
    ordering_fields = ['birth_year', 'name']
    ordering = ['id']


    def perform_create(self, serializer):
        owner_profile = self.request.user.clinic_owners.first()
        if not owner_profile:
            raise exceptions.PermissionDenied(
                "You do not have an associated Owner profile. Please create an Owner profile first before adding pets."
            )
        serializer.save(owner=owner_profile)


class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    filterset_fields = ['pet', 'cost']
    search_fields = ['diagnosis', 'treatment', 'pet__name']
    ordering_fields = ['cost', 'date_created']
    ordering = ['id']

    @action(detail=False, methods=['get'])
    def expensive(self, request):
        expensive_records = self.get_queryset().filter(cost__gt=3000)
        serializer = self.get_serializer(expensive_records, many=True)
        return Response(serializer.data)
