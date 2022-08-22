from django.db import models


class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    skill = models.TextField()

    class Meta:
        verbose_name_plural = '1. Teacher'

    def __str__(self):
        return self.full_name


class CourseCategory(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = '3. Couser Category'

    def __str__(self):
        return self.title


class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name_plural = '4. Couser'

    def __str__(self):
        return "["+self.title+"] "+self.category.title


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    interested = models.TextField()

    class Meta:
        verbose_name_plural = '2. Student'

    def __str__(self):
        return self.full_name
