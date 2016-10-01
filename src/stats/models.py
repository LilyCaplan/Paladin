from django.db import models
# Create your models here.
class Stats(models.Model):
    Attorneys= models.CharField(max_length=120,blank=False, null=False)
    Hours= models.SmallIntegerField(null=False)
    Completed_Projects= models.SmallIntegerField(null=False)

    def __unicode__(self):
        return self.Attorneys
        return self.Hours
        return self.Completed_Projects

class Nonprofit_Partner(models.Model):
    Nonprofit= models.CharField(default="",max_length=100, null=False)

    def __unicode__(self):
        return self.Nonprofit

class Opportunity_Request(models.Model):
    Attorneys_Who_Request=models.CharField(default="", max_length=120,blank=False, null=False)
    Requested_Cases=models.CharField(default="", max_length=120,blank=False, null=False)

    def __unicode__(self):
        return self.Attorneys_Who_Request
        return self.Requested_Cases

class Attorney_List(models.Model):
    Attorneys=models.CharField(max_length=120,blank=False, null=False)
    Status= models.CharField(max_length=50,blank=False, null=False)
    Cases=models.CharField(max_length=120,blank=False, null=False)
    #This is really where the problem isI added a Date time field and it
    #just wont let me migrate anything else anymore
    # Timestamp field should go here
    # Total Hours Should go here


    def __unicode__(self):
        return self.Attorneys
        return self.Status
        return self.Cases



