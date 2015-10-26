import os
import jinja2
import model

currDir = os.path.dirname( os.path.abspath(__file__) )
parentDir = os.path.abspath(os.path.join(currDir, '..'))
viewDir = parentDir + os.path.sep + "view"
modelDir = parentDir + os.path.sep + "model"

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(viewDir),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)

MODEL = model.Model(
    modelDir + os.path.sep + "config.txt"
)