from django.db import models
#from django.db.transaction import managed

# Create your models here.

GENDERS = (
          ('male', 'Male'),
          ('female', 'Female'),
)

ACTIVITY_LEVELS = (
                   (1.25, 'Sedentary'),
                   (1.3, 'Lightly Active'),
                   (1.5, 'Moderately Active'),
                   (1.7, 'Very Active'),
                   (2.0, 'Extremely Active'),
)

SERVING_TYPES = (
                 ('ounce', 'Ounce'),
                 ('cup', 'Cup'),
                 ('pound', 'Pound'),
                 ('pint', 'Pint'),
                 ('tablespoon', 'Tablespoon'),
                 ('teaspoon', 'Teaspoon'),
                 ('gram', 'Gram'),
                 ('CUSTOM', 'CUSTOM'),
)

YES_NO_FLAGS = (
                ('Y', 'Y'),
                ('N', 'N'),
)

class User(models.Model):
    gender = models.CharField(max_length=7, choices=GENDERS)
    age = models.IntegerField()
    height_in_inches = models.FloatField()
    activity_level = models.FloatField(choices=ACTIVITY_LEVELS)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    active = models.CharField(max_length=1, choices=YES_NO_FLAGS)
    
    def __unicode__(self):
        return self.first_name + " " + self.last_name
    
    class Meta:
        db_table = 'users'
        ordering = ['username']
        managed = False
    

class Weight(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField()
    pounds = models.FloatField()
    
    def __unicode__(self):
        return self.user.username + ", " + self.date.strftime("%Y-%m-%d") + ", " + str(self.pounds)
    
    class Meta:
        db_table = 'weight'
        unique_together = (("user", "date"),)
        ordering = ['user', '-date']
        managed = False
            

class Food(models.Model):
    name = models.CharField(max_length=50)
    default_serving_type = models.CharField(max_length=20, choices=SERVING_TYPES)
    serving_type_qty = models.FloatField()
    calories = models.IntegerField()
    fat = models.FloatField()
    saturated_fat = models.FloatField()
    carbs = models.FloatField()
    fiber = models.FloatField()
    sugar = models.FloatField()
    protein = models.FloatField()
    sodium = models.FloatField()

    def __unicode__(self):
        return self.name + " - " + str(self.serving_type_qty) + " " + self.default_serving_type

    class Meta:
        db_table = 'foods'
        ordering = ['name']
        managed = False

    
class FoodEaten(models.Model):
    user = models.ForeignKey(User)
    food = models.ForeignKey(Food)
    date = models.DateField()
    serving_type = models.CharField(max_length=20, choices=SERVING_TYPES)
    serving_qty = models.FloatField()
    
    def __unicode__(self):
        return self.user.username + ", " + self.date.strftime("%Y-%m-%d") + " - " + self.food.name + " " + str(self.serving_qty) + " " + self.serving_type 
    
    class Meta:
        db_table = 'foods_eaten'
        unique_together = (("user", "food", "date"),)
        ordering = ['user', '-date']
        managed = False
        

class Exercise(models.Model):
    name = models.CharField(max_length=50)
    calories_per_hour = models.IntegerField()
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'exercises'
        ordering = ['name']
        managed = False
        
        
class ExercisePerformed(models.Model):
    user = models.ForeignKey(User)
    exercise = models.ForeignKey(Exercise)
    date = models.DateField()
    minutes = models.IntegerField()
    
    def __unicode__(self):
        return self.user.username + ", " + self.date.strftime("%Y-%m-%d") + " - " + self.exercise.name
    
    class Meta:
        db_table = 'exercises_performed'
        unique_together = (("user", "exercise", "date"),)
        ordering = ['user', '-date']
        managed = False 
