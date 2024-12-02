from django.db import models

class ContactMessage(models.Model):
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class GalleryImage(models.Model):
    user_email = models.EmailField()
    image = models.ImageField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_email} - {self.image.name}"
