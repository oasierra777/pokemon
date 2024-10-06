from pkm.settings import local
from django.core.exceptions import PermissionDenied

class IPBlackListMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response

    
    def __call__(self, request):
        if hasattr(local, 'BANNED_IPS') and local.BANNED_IPS is None:
            #comprobar si la dirección ip de la petición entrante está en las ips prohibidas
            if request.META['REMOTE_ADDR'] in local.BANNED_IPS:
                raise PermissionDenied()
        response = self.get_response(request)
        return response
