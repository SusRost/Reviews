# review_app/models.py

from django.db import models

class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    sentiment = models.CharField(max_length=3)
    timestamp = models.DateTimeField(auto_now_add=True)  # Используем auto_now_add для автоматического добавления времени создания

    def __str__(self):
        return f"Review #{self.id} - {self.sentiment}"
