from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from .serializers import MessageSerializer
from .services import create_message, get_messages

class MessageViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = MessageSerializer
    def get_queryset(self):
        # queryset нужен DRF для schema/browsable API
        # Реальную пагинакцию делает get_messages() в list()
        from .models import Message
        return Message.objects.all()
    def list(self, request, *args, **kwargs):
        page_number = request.query_params.get('page', 1)
        page = get_messages(page=page_number)
        serializer = self.get_serializer(page.object_list, many=True)
        paginator = page.paginator
        base_url = request.build_absolute_uri(request.path)

        next_url = None
        prev_url = None
        if page.has_next():
            next_url = f"{base_url}?page={page.next_page_number()}"
        if page.has_previous():
            prev_url = f"{base_url}?page={page.previous_page_number()}"

        return Response({
            'count': paginator.count,
            'next': next_url,
            'previous': prev_url,
            'results': serializer.data,
        })

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        message = create_message(
            object=serializer.validated_data['object'],
            text=serializer.validated_data['text'],
        )

        out = self.get_serializer(message)
        return Response(out.data, status=status.HTTP_201_CREATED)

