from django.db import models

class Feature(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Challenge(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Outcome(models.Model):
    outcome = models.TextField(max_length=1000, unique=True)

    def __str__(self):
        return self.outcome

class Project(models.Model):
    proj_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    proj_area = models.CharField(max_length=200)
    proj_type = models.CharField(max_length=200, choices=[
        ('Residential', 'Residential'),
        ('Commercial', 'Commercial'),
        ('Industrial', 'Industrial'),
        ('Mixed Use', 'Mixed Use'),
        ('Other', 'Other')
    ])
    proj_status = models.CharField(max_length=200, choices=[
        ('Planning', 'Planning'),
        ('Under Construction', 'Under Construction'),
        ('Completed', 'Completed'),
        ('On Hold', 'On Hold'),
        ('Cancelled', 'Cancelled')
    ])
    proj_duration = models.CharField(max_length=200)
    professionals = models.IntegerField()
    proj_budget = models.DecimalField(max_digits=10, decimal_places=2)
    completed_date = models.CharField(max_length=200, null=True, blank=True)
    client_name = models.CharField(max_length=200)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True, null=True, max_length=1000)

    features = models.ManyToManyField(Feature, related_name='features_projects', blank=True)
    challenges = models.ManyToManyField(Challenge, related_name='challenges_projects', blank=True)
    outcomes = models.ManyToManyField(Outcome, related_name='projects', blank=True)
    
    def __str__(self):
        return self.proj_name

class projimage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    img = models.ImageField(upload_to='project_images/')
