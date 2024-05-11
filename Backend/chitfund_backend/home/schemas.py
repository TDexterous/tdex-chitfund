from .models import Songs
from ninja import ModelSchema, Schema


class SongsSchema(ModelSchema):
    class Meta:
        model = Songs
        fields = ['id', 'title', 'artist', 'duration', 'last_play']


class NotFoundSchema(Schema):
    message: str
