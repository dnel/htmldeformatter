from bottle import Bottle, run, template, request, static_file
from beaker.middleware import SessionMiddleware
from os.path import abspath, dirname, join
import html2text
app = Bottle()

#
# Beaker cookie handler configuration
#

session_options = {
    'session.type': 'file',
    'session.data_dir': './session/',
    'session.auto': True,
}

app_middleware = SessionMiddleware(app, 
                                   session_options)

@app.hook('before_request') 
def setup_request():
    """
    pre-assign request.session for cookie access before every 
    request
    """
    request.session = request.environ['beaker.session']
#
# Static files configuration for CSS, Javascript etc
#

appPath = dirname(abspath('__file__'))

@app.route('/static/css/:filename#.*#', name='css')
def server_static(filename):
    return static_file(filename, 
                       root=join(appPath,'static/css'))
    
@app.route('/static/js/:filename#.*#', name='js')
def server_static(filename):
    return static_file(filename, 
                       root=join(appPath,'static/js'))
    
@app.route('/static/img/:filename#.*#', name='images')
def server_static(filename):
    return static_file(filename, 
                       root=join(appPath,'static/img'))

#
# Routing for requests
#
@app.route('/')
@app.post('/')
def main():
    output_text = ""
    if request.forms.html_content:
        h = html2text.HTML2Text()
        h.ignore_links = True
        html_content = request.forms.html_content
        output_text = h.handle(html_content)
    return template("index",
                    converted_text=output_text,
	                get_url=app.get_url)

#
# Launch the app!
#
	
if __name__ == "__main__": run(app_middleware, 
							   host="localhost", 
							   port=8080, 
							   debug=True, 
							   reloader=True)
