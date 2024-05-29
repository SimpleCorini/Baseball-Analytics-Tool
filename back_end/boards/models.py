from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models import F

User = get_user_model()


class Article(models.Model):
    post_id = models.AutoField(primary_key=True, verbose_name='게시글 아이디')
    title = models.TextField(verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    upd_date = models.DateTimeField(null=True, verbose_name='수정일')
    count = models.IntegerField(default=0, verbose_name='조회수')
    type_team = models.CharField(max_length=255, verbose_name='팀 분류')
    nickname = models.CharField(max_length=100, verbose_name='유저 이름')
    like_count = models.IntegerField(default=0, verbose_name='좋아요 수')

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField(verbose_name='내용')
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    upd_date = models.DateTimeField(null=True, blank=True, verbose_name='수정일')
    post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name='게시글')
    nickname = models.CharField(max_length=100, verbose_name='유저 이름')
    like_count = models.IntegerField(default=0, verbose_name='좋아요 수')
    def __str__(self):
        return f"Comment by {self.nickname} on {self.post.title}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'content_type', 'object_id')

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            self.content_object.like_count = F('like_count') + 1
            self.content_object.save(update_fields=['like_count'])

    def delete(self, *args, **kwargs):
        self.content_object.like_count = F('like_count') - 1
        self.content_object.save(update_fields=['like_count'])
        super().delete(*args, **kwargs)
