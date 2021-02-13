from djongo import models
# from pymongo import MongoClient

""" 
def get_db_collection():
    cluster = MongoClient(
    )
    db = cluster['fullThrottleDB']
    collection = db['user-activity']
    return collection
"""


class User(models.Model):
    id = models.CharField(
        max_length=100,
        blank=False,
        primary_key=True
    )
    real_name = models.CharField(
        max_length=100,
        blank=False
    )
    tz = models.CharField(
        max_length=200,
        blank=False
    )

    def __str__(self):
        return '{} {} {}'.format(self.id, self.real_name, self.tz)

# many-to-one relationship with User model
# added foreignKey to associate multiple records to single user


class ActivityPeriod(models.Model):
    activity_id = models.AutoField(
        primary_key=True,
        blank=False
    )
    start_time = models.DateTimeField(
        blank=False
    )
    end_time = models.DateTimeField(
        blank=False
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '{} {}'.format(self.start_time, self.end_time)
