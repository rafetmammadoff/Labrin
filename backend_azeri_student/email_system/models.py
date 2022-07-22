from django.db import models


# Create your models here.
class EmailData(models.Model):
    full_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255)
    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.full_name)

    class Meta:
        ordering = ('full_name',)


class EmailHistory(models.Model):
    email = models.EmailField()
    template = models.ForeignKey('EmailTemplate', on_delete=models.CASCADE,
                                 null=True, blank=True)
    status = models.BooleanField(default=False)

    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.email)

    class Meta:
        ordering = ('-id',)


class EmailTemplate(models.Model):
    name = models.CharField(max_length=255)
    context = models.TextField()

    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        ordering = ('-id',)