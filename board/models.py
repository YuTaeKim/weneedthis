from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor_uploader.fields import RichTextUploadingField



class User(AbstractUser):
    thinker_likes=models.IntegerField(default=0)
    thinker_status=models.CharField(max_length=20,default='꿈나무')

    def __str__(self):
        return self.username

    def update_thinker_status(self):
        if self.thinker_likes>19:
            self.thinker_status='혁신가'
            self.save()
        else:
            self.thinker_status='꿈나무'
            self.save()

    @property
    def total_ideas(self):
        return self.idea.count()

    @property
    def total_ideas_likes(self):
        return self.idea_likes.count()
    
    @property
    def total_comments(self):
        return self.comment.count()

    @property
    def total_comments_likes(self):
        return self.comment_likes.count()
    

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

class Motivation(form):
    author=models.ForeignKey('User',on_delete=models.CASCADE,related_name='motivation')
    title=models.CharField(max_length=100)
    likes=models.ManyToManyField('User',related_name='motivation_likes',blank=True)

    def __str__(self):
        return self.author.username+' - '+self.title

    @property
    def total_likes(self):
        return self.likes.count() 




class form2(models.Model):
    article=models.TextField()
    pub_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract=True
        ordering=['pub_date']



class Comment(form2):
    for_idea=models.ForeignKey('Idea',on_delete=models.CASCADE,related_name='comment')
    reply_to=models.ForeignKey('self',on_delete=models.CASCADE,related_name='replies',blank=True,null=True)
    author=models.ForeignKey('User',on_delete=models.CASCADE,related_name='comment')
    likes=models.ManyToManyField('User',related_name='comment_likes',blank=True)

    def __str__(self):
        return self.author.username+' - '+self.article

    @property
    def total_likes(self):
        return self.likes.count()


class Message(form2):
    sender=models.ForeignKey('User',on_delete=models.CASCADE,related_name='send_message')
    receiver=models.ForeignKey('User',on_delete=models.CASCADE,related_name='receive_message')

    def __str__(self):
        return 'sender:'+self.sender.username+', receiver:'+self.receiver.username+' - '+self.article







