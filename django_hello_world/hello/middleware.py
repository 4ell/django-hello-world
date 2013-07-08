from json import dumps
from models import ReqData


class RequestStoringMiddleware:
    def process_request(self, request):
        data = ReqData()
        data.path = request.path
        data.get = dumps(request.GET)
        data.post = dumps(request.POST)
        data.cookies = dumps(request.COOKIES)
        data.save()
