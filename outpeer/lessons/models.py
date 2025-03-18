from django.db import models
from users.models import Course

class Lesson(models.Model):
    title = models.CharField(max_length=255)  
    content = models.TextField()  
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")  
    video_url = models.URLField(blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.title

