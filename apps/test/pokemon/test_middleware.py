from django.test import TestCase, override_settings
from django.contrib.auth.models import User
from http import HTTPStatus

class IPBlacklistMiddlewareTest(TestCase):
    """Middlewera para acceder a la api se debe estaer logeado
    la lista negra es para la ip 127.0.0.1 y se pude modificar la ip segun sea necesario
    Args:
        TestCase (Lista negra): prueba de lista negra 
    """
    
    def setUp(self):
        self.user = User()
        
    @override_settings(BANNED_IPS=None)
    def test_request_successful_without_blacklist_settings(self):
        response = self.user.get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
    
    @override_settings(BANNED_IPS=['192.168.1.2'])
    def test_request_successful_without_non_blacklist_settings(self):
        response = self.user.get('/', REMOTE_ADDR="192.100.1.3")
        self.assertEqual(response.status_code, HTTPStatus.OK)