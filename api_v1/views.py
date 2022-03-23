import json
from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render


def echo_view(request):
    response_data = {
        "method": request.method,
        "datetime": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    print(request.body)
    if request.body:
        response_data["body"] = json.loads(request.body)

    response = JsonResponse(response_data)

    return response
