from application import db

class TopImageModel(db.Model):
    __tablename__ = "top_image"
    id = db.Column(db.SMALLINT, primary_key=True, comment="顶图id")
    url = db.Column(db.String(64), comment="顶图url")