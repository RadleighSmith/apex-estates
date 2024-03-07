from django.db import models

class Message(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class NewsletterSignUp(models.Model):
    email = models.EmailField()
    sign_up_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email