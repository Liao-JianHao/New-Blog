import random
from flask_restful import Resource


from .models import TopImageModel


class TopImage(Resource):
    def get(self):
        image_list = TopImageModel.query.all()
        image = image_list[random.randint(1, len(image_list))-1]
        return {"image_url": image.url}