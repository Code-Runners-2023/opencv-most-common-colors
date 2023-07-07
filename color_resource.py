from flask import abort
from flask_restful import Resource, request
from color_picker import ColorPicker

class ColorResource(Resource):
    def __init__(self):
        super().__init__()
        self.color_picker = ColorPicker()

    def post(self, colors_count):
        file = request.files['file']

        try:
            colors_count = int(colors_count)
        except:
            abort(400, "colors_count should be a number in range 1 to infinity")

        if not file:
            abort(400, "You should pass file!")

        if colors_count < 1:
            abort(400, "You should pass a valid colors_count greater than or equal to 1!")

        return self.color_picker.get_colors(file, colors_count), 200