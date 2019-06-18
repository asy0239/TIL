from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill    # Resizeing 하는 이유는 사용자에게 파일을,# 그대로 제공하지말고 썸네일 식으로 제공
from django.conf import settings



# Create your models here.
class Post(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_posts")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    # image = models.ImageField(blank=True)  ## blank 는 이미지를 안넣고 migrate 가 가능
    image = ProcessedImageField(
        upload_to='posts/images',                 ## 올리는 위치 설정
        processors=[ResizeToFill(600, 600)],       ## 사이즈를 정한다.
        format='JPEG',
        options={'quality': 90}
    )


class Comment(models.Model):
    content = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
