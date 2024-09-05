# views.py
from django.http import JsonResponse
from .models import Consignment

def consignment_details(request, pk):
    try:
        consignment = Consignment.objects.get(pk=pk)
        data = {
            'supplier': consignment.supplier,
            'invoice_number': consignment.invoice_number,
            'location': consignment.location.id,
        }
        return JsonResponse(data)
    except Consignment.DoesNotExist:
        return JsonResponse({'error': 'Consignment not found'}, status=404)
