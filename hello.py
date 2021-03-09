def wsgi_application(environ, start_response):
   status = '200 OK'
   headers = [('Content-Type', 'text/plain')]
   body = [bytes(str((i + "\r\n") for i in environ['QUERY_STRING'][2:].split('&')), 'utf-8')]
   start_response(status, headers)
   return body

