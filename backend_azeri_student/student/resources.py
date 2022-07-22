from import_export import resources
from student.models import ContactUs

class ContactUsResource(resources.ModelResource):

    class Meta:
        model = ContactUs
        fields = '__all__'