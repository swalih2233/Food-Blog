from django.db import models
from django.contrib.auth.models import User



class Categery(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'blo_categery'
        verbose_name = 'categery'
        verbose_name_plural = 'categories'
        ordering = ('-id',)

    def __str__(self):
        return self.name



class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'blo_author'
        verbose_name = 'author'
        verbose_name_plural = 'author'
        ordering = ('-id',)

    def __str__(self):
        return self.user.username



class Tag(models.Model):
    name = models.CharField(max_length=100)


    class Meta:
        db_table = 'blo_tag'
        verbose_name = 'tag'
        verbose_name_plural = 'tag'
        ordering = ('-id',)

    def __str__(self):
        return self.name



class Blog(models.Model):
    title = models.CharField(max_length=100)
    short_description =models.CharField(max_length=100)
    author =models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="blog")
    description = models.TextField()
    categery = models.ForeignKey(Categery, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)


    
    class Meta:
        db_table = 'blo_blog'
        verbose_name = 'blog'
        verbose_name_plural = 'blog'
        ordering = ('-id',)

    def __str__(self):
        return self.title


    
