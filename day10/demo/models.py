from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20, unique=True)
    pwd = models.CharField(max_length=128)
    age = models.IntegerField()
    gender = models.CharField(choices=(('0', '男'), ('1', '女')), max_length=1)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.name


class Token(models.Model):
    key = models.CharField(max_length=128)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='token')

    class Meta:
        db_table = 'token'

    def __str__(self):
        return self.user.name


class Comment(models.Model):
    content = models.TextField()
    addtime = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')

    class Meta:
        db_table = 'comment'

    def __str__(self):
        return self.content
