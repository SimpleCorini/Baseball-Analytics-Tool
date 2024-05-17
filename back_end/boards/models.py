from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Article(models.Model):
    post_id = models.AutoField(primary_key=True, verbose_name='게시글 아이디')
    title = models.TextField(verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    upd_date = models.DateTimeField(null=True, verbose_name='수정일')
    count = models.CharField(max_length=255, default=0,verbose_name='조회수')
    type_team = models.CharField(max_length=255, verbose_name='팀 분류')
    nickname = models.CharField(max_length=100, verbose_name='유저 이름')

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField(verbose_name='내용')
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    upd_date = models.DateTimeField(null=True, blank=True, verbose_name='수정일')
    post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name='게시글')
    nickname = models.CharField(max_length=100, verbose_name='유저 이름')

    def __str__(self):
        return f"Comment by {self.nickname} on {self.post.title}"
