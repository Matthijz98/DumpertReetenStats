from django.core.management.base import BaseCommand, CommandError
from reetenstats.models import Video
import time


class Command(BaseCommand):
    help = 'Update video thumnails'

    def handle(self, *args, **options):
        videos = Video.objects.all().filter(video_thumbnail=None, video_dumpert_id__isnull=False)

        for video in videos:
            print(f"Update {video.video_title}")
            video.get_thumbnail()
            print("wait 5 seconds")
            time.sleep(5)