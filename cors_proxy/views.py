from django.shortcuts import render
import json
# Create your views here.

import requests
from django.http import JsonResponse

def proxy_view(request):
    if request.method == 'OPTIONS':
        # Handle preflight CORS requests
        response = JsonResponse({})
        # response["Access-Control-Allow-Origin"] = "*"
        # response["Access-Control-Allow-Methods"] = "GET, OPTIONS" 
        return response

    elif request.method == 'GET':
        # Forward the GET request to the external API
        req_url = request.GET.get('url', '')  # Replace with your API URL
        #print('url = ', req_url)
        response = requests.get(req_url)

        # Create a response with the API response content and CORS headers
        #content = response.content
        # response_headers = response.headers
        # response_headers["Access-Control-Allow-Origin"] = "*"
        # response_headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        # response_headers["Access-Control-Allow-Headers"] = "Content-Type, Connection"
        # del response_headers["Content-Type"]
        # del response_headers["Connection"]
        # print('head = ', response_headers)
        # res_str = content.decode("utf-8")
        # print(res_str)
        # res = json.loads(res_str)
        # print(res) 
        return JsonResponse(response.json(), safe=False, status=response.status_code)

    else:
        # Handle other HTTP methods as needed
        return JsonResponse({'error': 'Method not allowed'}, status=405)

