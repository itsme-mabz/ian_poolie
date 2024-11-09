from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

@api_view(['POST'])
def process_and_forward_data(request):
    incoming_data = request.data
    processed_data = {
        "firstName": incoming_data.get("firstname", ""),
        "lastName": incoming_data.get("lastname", ""),
        "displayName": f"{incoming_data.get('firstname', '')} {incoming_data.get('lastname', '')}",
        "address": incoming_data.get("address", ""),
        "city": incoming_data.get("city", ""),
        "state": incoming_data.get("state", ""),
        "zipcode": incoming_data.get("zip", ""),
        "contactNumber": incoming_data.get("phone", ""),
        "email": incoming_data.get("email", ""),
        "GateCode": incoming_data.get("gate_code_", ""),
        "accessNotes": incoming_data.get("maintenance_notes", ""),
        "hasDogs": "yes"
    }

    external_api_url = "https://prodapi.poolbrain.com/create_customer"
    headers = {
        "Content-Type": "application/json",
        "ACCESS-KEY": "6d1ce5a72aaf"
    }

    try:
        response = requests.post(external_api_url, json=processed_data, headers=headers)
        response_data = response.json()
        status_code = response.status_code
    except requests.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(response_data, status=status_code)
