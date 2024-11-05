from django.db import models

# Create your models here.
class command(models.Model):
    name= models.TextField()
    job= models.TextField()
    age= models.TextField()
    employed= models.BooleanField()

def create_info(name,job,age,employed):
    student = command.objects.create(name=name, job=job, age=age, employed= employed)
    student.save()
    return student
def view_all_info():
    return command.objects.all()
def view_cert_info(name):
    try:
        return command.objects.get(name=name)
    except:
        return None
def employed_command():
    return command.objects.filter(employed=True)
def update_info(name, is_employed, employed):
    command.objects.filter(name=name).update(job=is_employed, employed= employed)
def delete_info(name):
    command.objects.filter(name=name).delete()