from django.db import models

# Create your models here.
class Blog(models.Model):
    """
    TODO usar el objeto de User predefinido por Django
    """
    user = models.CharField(max_length=50, default="Usuario@test.com")
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/img/')
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title