from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    place = models.CharField(max_length=100)
    when_datetime = models.DateTimeField()
    trainer = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return ', '.join([self.place, self.trainer, str(self.when_datetime), str(self.capacity)])
    
    def free_slots(self) -> int:
        temp_result = self.capacity - len(self.participant_set.all())
        return 0 if temp_result < 0 else temp_result
    
class Participant(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True)
    note = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
