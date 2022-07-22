# from django.db import models
#
# # Create your models here.
# from base_user.tools.common import GENDER
# from crmstudent.tools.common import DEGREE, CERTIFICATIONS, STATUS
# from student.models import Country
#
#
# class StudentInformation(models.Model):
#     withparent = models.BooleanField('Valideynlə birgə gəlib', default=False,
#                                      help_text='Əgər tələbə valideyn birgə gəlibsə'
#                                                ' o zaman bu sahəni check edin')
#     first_name = models.CharField('Ad', max_length=200)
#     last_name = models.CharField('Soyad', max_length=200)
#     birth_date = models.DateField('Doğum tarixi')
#     phone = models.CharField('Əlaqə nömrəsi', help_text='Əgər tələbə valideyn '
#                                                         'birgə gəlibsə o zaman bu sahəni boş keçə bilərsiniz',
#                              null=True, blank=True, max_length=100)
#     email = models.EmailField('Email', help_text='Əgər tələbə valideyn birgə gəlibsə o zaman bu sahəni boş keçə '
#                                                  'bilərsiniz', null=True, blank=True)
#     gender = models.PositiveIntegerField('Cinsi', choices=GENDER, default=1)
#     picture = models.ImageField('Şəkil', upload_to='student/picture')
#     status = models.PositiveIntegerField(choices=STATUS, default=1)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __init__(self, *args, **kwargs):
#         super(StudentInformation, self).__init__(*args, **kwargs)
#         self.cache_status = self.status
#
#     def __str__(self):
#         return "{} {}".format(self.first_name, self.last_name)
#
#     class Meta:
#         verbose_name = 'Tələbə haqqında məlumat'
#         verbose_name_plural = 'Tələbələr haqqında məlumat'
#
#
# class Educations(models.Model):
#     fk = models.ForeignKey('StudentInformation', related_name='educations_student_information')
#     name = models.ForeignKey('Universities', verbose_name='Müəssisənin adı', related_name='education_universities')
#     degree = models.PositiveIntegerField('Dərəcə', choices=DEGREE, default=1)
#     faculty = models.CharField('Fakültə/Ixtisas', max_length=250)
#     start_date = models.DateField('Başlama tarixi')
#     end_date = models.DateField('Bitirmə tarixi')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Təhsil müəssisəsi haqqında məlumat'
#         verbose_name_plural = 'Təhsil müəssisələri haqqında məlumat'
#
#
# class Universities(models.Model):
#     name = models.CharField('Adı', max_length=200)
#     address = models.TextField('Ünvan', null=True, blank=True, help_text='Vacib Sahə deyil')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Təhsil müəssisəsi'
#         verbose_name_plural = 'Təhsil müəssisələri'
#
#
# class Certifications(models.Model):
#     fk = models.ForeignKey('StudentInformation', related_name='certifications_student_information')
#     name = models.PositiveIntegerField('Sertifikatın adı', choices=CERTIFICATIONS, default=1)
#     score = models.CharField('Nəticə', max_length=100)
#     deadline = models.DateField('Bitmə tarixi')
#     file = models.FileField('Fayl', upload_to='certification/file', null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Tələbənin sertifikatları'
#         verbose_name_plural = 'Tələbələrin sertifikatları'
#
#
# class PriceRanges(models.Model):
#     start_price = models.PositiveIntegerField('Qiymet aralığının başlanğıc qiyməti', default=100)
#     end_price = models.PositiveIntegerField('Qiymet aralığının son qiyməti', default=200)
#     currency = models.CharField('Valyuta', max_length=200)
#
#     def __str__(self):
#         return " {} - {} {}".format(self.start_price, self.end_price, self.currency)
#
#     class Meta:
#         verbose_name = 'Pul aralığı'
#         verbose_name_plural = 'Pul aralığı'
#
#
# class UniversityInformation(models.Model):
#     fk = models.ForeignKey('StudentInformation', related_name='university_student_information')
#     country = models.ForeignKey(Country, verbose_name='Təhsil almaq istədiyiniz ölkə',
#                                 related_name='country_university_informations')
#     degree = models.PositiveIntegerField('Dərəcə', choices=DEGREE, default=1)
#     specialty = models.CharField('Təhsil almaq istədiyiniz ixtisas', max_length=300)
#     date_interval = models.DateField('Təhsil alacağınız tarix')
#     price_interval = models.ForeignKey('PriceRanges', related_name='price_interval_university')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.country.name
#
#     class Meta:
#         verbose_name = 'Təhsil almaq istədiyi müəssisə ilə bağlı'
#         verbose_name_plural = 'Təhsil almaq istədiyi müəssisə ilə bağlı'
#
#
# class ParentInformation(models.Model):
#     fk = models.ForeignKey('StudentInformation', related_name='parent_student_information')
#     full_name = models.CharField('Valideynin tam adı', max_length=200)
#     phone = models.CharField('Telefon nömrəsi', max_length=200)
#     email = models.EmailField('Email', null=True, blank=True,
#                               help_text='Əgər tələbənin emaili qeyd olunmayıbsa bu sahəni doldurun')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.full_name
#
#     class Meta:
#         verbose_name = 'Valideyn haqqında'
#         verbose_name_plural = 'Valideynlər haqqında'
#
#
# class AutoReplayMessage(models.Model):
#     subject = models.CharField('Subject', max_length=200)
#     types = models.PositiveIntegerField(choices=STATUS, default=1, help_text='Seçilmiş status auto replay'
#                                                                              ' mətini uyğun olaraq'
#                                                                              ' gönderiləcək')
#     content = models.TextField('Content')
#
#     def __str__(self):
#         return self.subject
#
#     class Meta:
#         verbose_name = 'Avtomatik cavab mətini'
#         verbose_name_plural = 'Avtomatik cavab mətinləri'
#
#
# class SpecificityStudentMessage(models.Model):
#     subject = models.CharField('Subject', max_length=200)
#     types = models.PositiveIntegerField(choices=STATUS, default=1, help_text='Seçilmiş status uyğun metin gönderiləcək')
#     student = models.ForeignKey('StudentInformation', related_name='specificity_message_student_information')
#     content = models.TextField('Content')
#
#     def __str__(self):
#         return self.subject
#
#     class Meta:
#         verbose_name = 'Spesifik cavab mətini'
#         verbose_name_plural = 'Spesifik cavab mətinləri'