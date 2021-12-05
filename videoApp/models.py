from django.db import models


class VideoModel(models.Model):
    video_title = models.CharField(max_length=50)

    video_desc = models.TextField()

    def __str__(self):
        return 'name: {}, id: {} '.format(self.video_title, self.id)


