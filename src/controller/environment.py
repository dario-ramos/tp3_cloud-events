import os
import jinja2

currDir = os.path.dirname( os.path.abspath(__file__) )
parentDir = os.path.abspath(os.path.join(currDir, '..'))
viewDir = parentDir + os.path.sep + "view"
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(viewDir),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)