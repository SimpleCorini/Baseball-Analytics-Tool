from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    TEAM_CHOICES = [
        ('LG Twins', 'LG Twins'),
        ('KT Wiz', 'KT Wiz'),
        ('SSG Landers', 'SSG Landers'),
        ('NC Dinos', 'NC Dinos'),
        ('Doosan Bears', 'Doosan Bears'),
        ('Hanhwa Eagles', 'Hanhwa Eagles'),
        ('Lotte Giants', 'Lotte Giants'),
        ('KIA Tigers', 'KIA Tigers'),
        ('Samsung Lions', 'Samsung Lions'),
        ('Kiwoom Heroes', 'Kiwoom Heroes'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100)
    favorite_team = models.CharField(
        max_length=50,
        choices=TEAM_CHOICES,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Profile for {self.user.username}"


