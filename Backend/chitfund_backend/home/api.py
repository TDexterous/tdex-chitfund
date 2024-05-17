from ninja import NinjaAPI
from .schemas import SongsSchema, NotFoundSchema
from .models import Songs

app = NinjaAPI()


@app.get('songs/', response=list[SongsSchema])
def songs(request):
    return Songs.objects.all()


@app.get('song/{song_id}/', response={200: SongsSchema, 404: NotFoundSchema})
def get_song(request, song_id):
    try:
        song = Songs.objects.get(pk=song_id)
        return song
    except Songs.DoesNotExist as e:
        return 404, {'message': 'song does not exits'}

