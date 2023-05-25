from django.db import models
class Poll(models.Model):
    question = models.TextField(null=True)
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    
    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count
    
class objectsave(models.Model):

    option = models.CharField(max_length=30)

    def __str__(self):
        return self.option
    
#lass votemodel(models.Model):
