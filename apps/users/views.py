from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import Username

from .serializers import UserSerializers,RegisterUserSerializer

# Create your views here.
class UserAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.DestroyModelMixin):
    queryset = Username.objects.all()
    serializer_class = UserSerializers

    def get_serializer_class(self):
        if self.action in ('create', ):
            return RegisterUserSerializer
        # if self.action in ('retrieve', ):
        #     return UserDetailSerializer
        return UserSerializers

    