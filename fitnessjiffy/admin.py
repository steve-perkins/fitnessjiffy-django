from django.contrib import admin
from fitnessjiffy.models import User, Food, FoodEaten, Exercise, ExercisePerformed, Weight

admin.site.register(User)
admin.site.register(Weight)
admin.site.register(Food)
admin.site.register(FoodEaten)
admin.site.register(Exercise)
admin.site.register(ExercisePerformed)


