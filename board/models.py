from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor_uploader.fields import RichTextUploadingField



class User(AbstractUser):
    thinker_likes=models.IntegerField(default=0)
    thinker_status=models.CharField(max_length=20,default='꿈나무')

    def __str__(self):
        return self.username

    def update_thinker_status(self):
        likes=self.idea.total_likes+self.feedback.total_likes+self.comment.total_likes
        if likes>10:
            self.thinker_status='genius'
            self.save()

    @property
    def total_ideas(self):
        return self.idea.count()

    @property
    def total_ideas_likes(self):
        return self.idea_likes.count()
    

class form(models.Model):
    article=RichTextUploadingField()
    pub_date=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True
        ordering=['-pub_date']


class Idea(form):
    author=models.ForeignKey('User',on_delete=models.CASCADE,related_name='idea')
    title=models.CharField(max_length=100)
    likes=models.ManyToManyField('User',related_name='idea_likes',blank=True)
 
    def __str__(self):
        return self.author.username+' - '+self.title

    @property
    def total_likes(self):
        return self.likes.count() 


class Feedback(form):
    author=models.ForeignKey('User',on_delete=models.CASCADE,related_name='feedback')
    title=models.CharField(max_length=100)
    likes=models.ManyToManyField('User',related_name='feedback_likes',blank=True)
 
    def __str__(self):
        return self.author.username+' - '+self.title

    @property
    def total_likes(self):
        return self.likes.count() 


class Comment(form):
    author=models.ForeignKey('User',on_delete=models.CASCADE,related_name='comment')
    likes=models.ManyToManyField('User',related_name='comment_likes',blank=True)

    def __str__(self):
        return self.author.username+' - '+self.article

    @property
    def total_likes(self):
        return self.likes.count()

    





