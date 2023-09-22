import logging

logger = logging.getLogger('logging_mw')

class LoggingMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        http_method = request.method
        url = request.get_full_path()
        host_port = request.get_host()
        content_type = request.headers["Content-Type"]
        user_agent = request.headers['User-Agent']
        
        msg = f"{http_method} | {host_port}{url} | {content_type} | {user_agent}"
        logger.info(msg)
        
        response = self.get_response(request)


        headers = response.headers
        status_code = response.status_code
        
        msg = f"{status_code} | {headers}"
        logger.info(msg)

        return response
