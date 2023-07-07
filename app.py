from flask import Flask
from flask_restful import Api
from color_resource import ColorResource

app = Flask("ColorPickerAPI")
api = Api(app)
    
api.add_resource(ColorResource, '/colors/<colors_count>')

if __name__ == '__main__':
    app.run()