from response.requestHandler import RequestHandler
import os

class StaticHandler(RequestHandler):
    def __init__(self):
        self.filetypes = {
            ".js" : "text/javascript",
            ".css" : "text/css",
            ".jpg" : "image/jpeg",
            ".png" : "image/png",
            ".ico": "image/ico",
            "notfound" : "text/plain"
        }

    def find(self, file_path):
        split_path = os.path.splitext(file_path)
        extension = split_path[1]

        try: 
            print("public{}".format(file_path))

            if extension in (".jpg", ".jpeg", ".png", ".ico"):
                self.contents = open("src/public{}".format(file_path), 'rb')
            else:
                print('opening css...')
                self.contents = open("src/public{}".format(file_path), 'r')


            self.setContentType(extension)
            self.setStatus(200)
            return True
        #except:
        except Exception as e: 
            print(e)
            print("error")
            print("public{}".format(file_path))
            print(extension)
            self.setContentType('notfound')
            self.setStatus(404)
            return False

    def setContentType(self, ext):
      self.contentType = self.filetypes[ext]