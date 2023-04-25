from django.db import models

# Create your models here.
class HomeName(models.Model):

    name = models.CharField('Home name', max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-id']


class HomeImage(models.Model):

    img = models.ImageField('Home image', upload_to='grtnak')


class Contact(models.Model):

    username = models.CharField('User name', max_length=100)
    email = models.EmailField('User email')
    review = models.TextField('User review')

    def __str__(self):
        return self.username
    

class About(models.Model):

    name = models.CharField('About name', max_length=60)
    text = models.TextField('About text')

    def __str__(self):
        return self.text