from typing import Dict

from favorites.serializers import FavoritesSerializer
from cart.serializers import CartSerializer


class SessionObjectService:

    def __init__(self, object_name):
        self.object_name = object_name

    def get_or_create(self, request):
        """
        Retrieve cart cart from the session if exists else create new.
        """
        if self.object_name not in request.session:
            request.session[self.object_name] = {'items': []}
        return self.deserialize(request.session[self.object_name])

    def new(self, request):
        request.session[self.object_name] = {'items': []}
        request.session.modified = True

    def save(self, request, session_object) -> None:
        """
        Save cart to the session.
        """
        serialized_object = self.serialize(session_object)
        request.session[self.object_name] = serialized_object
        request.session.modified = True

    def serialize(self, session_object) -> Dict:
        """
        Serialize session object instance.
        """
        serializer = self._get_serializer()
        if serializer:
            return serializer(session_object).data
        else:
            return session_object

    def deserialize(self, session_object_data):
        serializer = self._get_serializer()
        if serializer:
            serializer = serializer(data=session_object_data)
            serializer.is_valid(raise_exception=True)
            return serializer.save()
        else:
            return session_object_data

    def _get_serializer(self):
        if self.object_name == 'cart':
            return CartSerializer
        elif self.object_name == 'favorites':
            return FavoritesSerializer
