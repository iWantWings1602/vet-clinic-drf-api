from rest_framework import generics
from .models import Pet, Owner
from .serializers import PetSerializer, OwnerSerializer


class PetListView(generics.ListAPIView):
    serializer_class = PetSerializer

    def get_queryset(self):
        queryset = Pet.objects.all()
        species = self.request.query_params.get('species')
        if species:
            queryset = queryset.filter(species=species)
        return queryset


class PetDetailView(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class OwnerListView(generics.ListAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class OwnerDetailView(generics.RetrieveAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class OwnerListCreateView(generics.ListCreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
