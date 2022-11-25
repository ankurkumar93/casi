from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_created=True)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title
    

class Inquiry(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.subject
    
    class Meta:
        verbose_name = 'Inquirie'