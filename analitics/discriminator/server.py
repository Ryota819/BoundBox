from bottle import route, run, static_file, request, response
from os import getenv, path
import json

from discriminator_pytorch import Discriminator
#from discriminator import Discriminator

def relative_path(target_path):
  return path.normpath(path.join(path.dirname(__file__), target_path))

@route('/')
def index():
  response.content_type = 'text/html; charset=utf-8'
  return static_file('index.html', root = relative_path('./'))

@route('/api/upload', method='POST')
def upload():
  upload = request.files.get('upload')
  result = discriminator.predict(upload.file)
  return json.dumps(result)

discriminator = Discriminator()

run(host='0.0.0.0', port=getenv('PORT', 8888), debug=True)
