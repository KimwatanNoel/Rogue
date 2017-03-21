from django.db import models


class Home(models.Model):
    Home_Photo = models.ImageField(upload_to='Blog_Photo')
    Title = models.TextField()
    Article = models.TextField()
    Author = models.TextField()
    Date_Created = models.DateField()

    def __str__(self):
        return self.Genre + self.Article + self.Author


class Fashion(models.Model):
    Fashion_Photo = models.ImageField(upload_to='Blog_Photo')
    Title = models.TextField()
    Article = models.TextField()
    Author = models.TextField()
    Date_Created = models.DateField()

    def __str__(self):
        return self.Title + self.Article + self.Author


class Technology(models.Model):
    Technology_Photo = models.ImageField(upload_to='Blog_Photo')
    Title = models.TextField()
    Article = models.TextField()
    Author = models.TextField()
    Date_Created = models.DateField()

    def __str__(self):
        return self.Genre + self.Article + self.Author


class Lifestyle(models.Model):
    Lifestyle_Photo = models.ImageField(upload_to='Blog_Photo')
    Title = models.TextField()
    Article = models.TextField()
    Author = models.TextField()
    Date_Created = models.DateField()

    def __str__(self):
        return self.Title + self.Article + self.Author


class Trending(models.Model):
    Trending_Photo = models.ImageField(upload_to='Blog_Photo')
    Title = models.TextField()
    Article = models.TextField()
    Author = models.TextField()
    Date_Created = models.DateField()

    def __str__(self):
        return self.Title + self.Article + self.Author


class Man_Talk(models.Model):
    Man_Talk_Photo = models.ImageField(upload_to='Blog_Photo')
    Title = models.TextField()
    Article = models.TextField()
    Author = models.TextField()
    Date_Created = models.DateField()

    def __str__(self):
            return self.Title + self.Article + self.Author


class Sports(models.Model):
    Sports_Photo = models.ImageField(upload_to='Blog_Photo')
    Title = models.TextField()
    Article = models.TextField()
    Author = models.TextField()
    Date_Created = models.DateField()

    def __str__(self):
            return self.Title + self.Article + self.Author








