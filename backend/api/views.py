from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def health_check(request):
    """Lightweight endpoint to confirm the API is running."""
    return Response({
        'status': 'ok',
        'message': 'Smart Cooking Recipe Assistant API is operational.',
    })
