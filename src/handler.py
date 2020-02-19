import os

from http.server import BaseHTTPRequestHandler

from response.staticHandler import StaticHandler
from response.templateHandler import TemplateHandler
from response.badRequestHandler import BadRequestHandler

from routers import routes
from pathlib import Path



class Handler(BaseHTTPRequestHandler):

  def do_HEAD(self):
    return

  def do_POST(self):
    return

  def do_GET(self):
    split_path = os.path.splitext(self.path)
    request_extension = split_path[1]

    if request_extension is "" or request_extension is ".html":
          if self.path in routes:
              handler = TemplateHandler()
              handler.find(routes[self.path])
          else:
              handler = BadRequestHandler()

    elif request_extension is ".py":
        handler = BadRequestHandler()        

    else:
      print('ERROR')
      handler = StaticHandler()
      handler.find(self.path)
 
      self.respond({
            'handler': handler
        })

    self.respond({'handler': handler})


  def handle_http(self, handler):
    status_code = handler.getStatus()
    self.send_response(status_code)

    if status_code is 200:
      content = handler.getContents()
      self.send_header('Content-type', handler.getContentType())
    else:
      content = "404 Not Found"

    self.end_headers()

    if isinstance( content, (bytes, bytearray) ):
      return content

    return bytes(content, 'UTF-8')

  def respond(self, opts):
    response = self.handle_http(opts['handler'])
    self.wfile.write(response)



