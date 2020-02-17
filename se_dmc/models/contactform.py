from django.db import models
from django.db.models.signals import post_save


class ContactForm(models.Model):
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=200, blank=False)
    subject = models.CharField(max_length=200, blank=False)
    message = models.TextField(max_length=500, blank=False)

    def __str__(self):
        return 'Message from {0} {1}\nemail {2}\nsubject {3}\nmessage {4} '.format(self.first_name, self.last_name, self.email, self.subject, self.message)


def save_post(sender, instance, **kwargs):
    print("working")


post_save.connect(save_post, sender=ContactForm)



