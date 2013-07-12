from django.db import models
from annoying.decorators import signals


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


class Action(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    model = models.CharField(max_length=30)
    action = models.CharField(max_length=10)
    object_id = models.IntegerField()

    def __unicode__(self):
        return '{0} {1}'.format(self.action, self.model)


@signals.post_save()
def savehandler(instance, **options):
    model = instance._meta.object_name
    action = 'create' if options['created'] else 'edit'
    if model == 'Action':
        return
    try:
        Action.objects.create(
            model=model,
            action=action,
            object_id=instance.id
        )
    except:
        return


@signals.post_delete()
def delhandler(instance, **options):
    model = instance._meta.object_name
    if model == 'Action':
        return
    try:
        Action.objects.create(
            model=model,
            action='delete',
            object_id=instance.id
        )
    except:
        return
