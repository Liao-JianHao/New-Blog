from flask import Blueprint
from flask_restful import Api


main = Blueprint('main', __name__)  # 创建main蓝图对象
api = Api(main)

# 路由设置
from .index.views import *
api.add_resource(TopImage, "/")
