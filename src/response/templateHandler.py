from response.requestHandler import RequestHandler

class TemplateHandler(RequestHandler):
    def __init__(self):
        super().__init__()
        self.contentType = 'text/html'

    def find(self, routeData):
        try:
            print('assets/templates/{}'.format(routeData['template']))
            template_file = open('src/assets/templates/{}'.format(routeData['template']))
            print("opening file...")
            self.contents = template_file
            self.setStatus(200)
            return True
        except:
            self.setStatus(404)
            return False