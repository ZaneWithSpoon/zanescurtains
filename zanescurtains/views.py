from django.http import JsonResponse, HttpResponse
import uuid, datetime, json



def test(request):
    print("testing")

    return JsonResponse({
            "status":"testing"
        })
