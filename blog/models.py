from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:50] + '...'

    def __str__(self) -> str:
        return self.title