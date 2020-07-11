from django.db import models
from django.utils import timezone
from django.db.models import Q

class ForTesting(models.Model):
    name = models.CharField('Name', max_length=50)
    description = models.CharField('Description', max_length=100)
    pub_date = models.DateTimeField(
        'Pub Date', auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    def recent(self):
        """Checks if a record is older than 30 days

        Returns:
            bool: the result of testing
        """
        now = timezone.now()
        delta = now - self.pub_date
        if delta.days <= 30:
            return True
        return False
        
class Book(models.Model):
    name = models.CharField(
        "Book",
        max_length=10
    )
    authors = models.ManyToManyField(
        ForTesting,
        related_name="books"
    )
    def __str__(self):
        return self.name
        
    
def q_constructor(some_conditions=None):

    q1 = Q(pk=3) & Q(name="name1")
    if some_conditions:
        q1 = q1 & Q(name="name2")
    return q1

ForTesting.objects.filter(q_constructor(True))


    


