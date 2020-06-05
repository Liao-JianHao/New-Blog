import json
from flask_restful import Resource


from .models import TopImageModel


class TopImage(Resource):
    def get(self):
        image_list = TopImageModel.query.all()
        image_dict = {}
        for image in image_list:
            image_dict[image.id] = image.url
        return {"msg": image_dict}