from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField()
    email = models.EmailField()
    jabber = models.CharField(max_length=30)
    skype = models.CharField(max_length=30)
    bio = models.TextField()
    contacts = models.TextField()
    photo = models.ImageField(upload_to='photos')

    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = Person.objects.get(id=self.id)
            if this.photo != self.photo:
                this.photo.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super(Person, self).save(*args, **kwargs)

    def __unicode__(self):
        return '{0} {1}'.format(self.name, self.last_name)


class ReqData(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    path = models.CharField(max_length=2048)
    get = models.TextField()
    post = models.TextField()
    cookies = models.TextField()

    def __unicode__(self):
        return '{0} {1}'.format(self.time, self.path)
