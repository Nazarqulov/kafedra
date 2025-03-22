

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
from PIL import Image
from django.utils import timezone
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')
class Salohiyat(models.Model):
    daraja=models.CharField(max_length=100)
    def __str__(self):
        return self.daraja
    class Meta:
        db_table = 'salohiyat'

QORALAMA="QORALAMA"
CHOP_ETISH="CHOP_ETISH"
tanlanma=(
    (QORALAMA, "QORALAMA"),
    (CHOP_ETISH, "CHOP_ETISH"),

)


class Muallim(models.Model):
    rasmi = models.ImageField(upload_to="images/")
    ismi = models.CharField(max_length=200)
    familiyasi = models.CharField(max_length=200)
    yoshi = models.IntegerField(default=1)
    ilmiy_salohiyati = models.ForeignKey(Salohiyat,max_length=100,on_delete=models.CASCADE)
    mutaxassisligi = models.CharField(max_length=200)
    yuklangan_sanasi = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=200)
    body = models.TextField()
    body_small = models.TextField()


    def __str__(self):
        return self.ismi

    class Meta:
        db_table = 'Muallim'
        verbose_name = 'Muallim'


class News(models.Model):
    class Status(models.TextChoices):
        Draft = "DRAFT",'df'
        Published = "PUBLISHED",'pd'
    nomi = models.CharField(max_length=200, verbose_name="yangliklar")
    rasmi = models.ImageField(upload_to="images/")
    xolat=models.CharField(max_length=120,choices=tanlanma,verbose_name="xolati")
    slug = models.SlugField(max_length=200)
    body = models.TextField()
    xolati=models.ForeignKey(Category,max_length=100,on_delete=models.CASCADE)
    create_time=models.DateTimeField(auto_now_add=True)
    publish_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=Status, default=Status.Draft)

    def save(self, *args, **kwargs):
        """Rasmni avtomatik ravishda bir xil o‘lchamga o'zgartirish"""
        super().save(*args, **kwargs)  # Dastlab rasmni saqlaymiz

        if self.rasmi:  # Agar rasm mavjud bo'lsa
            img_path = self.rasmi.path
            img = Image.open(img_path)

            max_size = (100, 100)  # Rasmning maksimal o‘lchami
            img = img.resize(max_size, Image.Resampling.LANCZOS)  # O'lchamni o'zgartirish

            img.save(img_path)  # O'zgartirilgan rasmni saqlash

    sana = models.DateTimeField(auto_now_add=True, verbose_name="sana", blank=True, null=True)
    izoh = models.TextField(max_length=2000, verbose_name="izoh")

    def __str__(self):
        return self.nomi

    class Meta:
        db_table = 'News'
        verbose_name = 'News'


class Loyihalar(models.Model):
    soxasi = models.CharField(max_length=200, verbose_name="soxasi")
    nomi = models.CharField(max_length=200, verbose_name="yangliklar")
    rasmi = models.ImageField(upload_to="images/")
    izoh = models.TextField(max_length=2000, verbose_name="izoh")

    def __str__(self):
        return self.nomi

    class Meta:
        db_table = 'Loyihalar'
        verbose_name = 'Loyihalar'


class Tadbirlar(models.Model):
    nomi = models.CharField(max_length=200, verbose_name="yangliklar")
    video = models.FileField(upload_to="images/")

    def __str__(self):
        return self.nomi

    class Meta:
        db_table = 'Tadbirlar'
        verbose_name = 'Tadbirlar'


class Talaba(models.Model):
    fullname = models.CharField(max_length=200, verbose_name="FISH")
    yoshi = models.IntegerField(default=1)
    rasmi = models.ImageField(upload_to="images/")
    izoh = models.TextField(max_length=2000, verbose_name="izoh")

    def __str__(self):
        return self.fullname

    class Meta:
        db_table = 'Talaba'


class Izohlar(models.Model):
    ismi = models.CharField(max_length=200)
    familiya = models.CharField(max_length=200)
    elektron_pochta = models.EmailField(max_length=200)
    tel_raqam = models.IntegerField(default=999)
    txt = models.TextField(max_length=2000)

    def __str__(self):
        return self.ismi

    class Meta:
        db_table = 'Izohlar'
        verbose_name = 'Izohlar'


class Registr(models.Model):
    ismi = models.CharField(max_length=200)
    familiya = models.CharField(max_length=200)
    elektron_pochta1 = models.CharField(max_length=200)
    phone = models.IntegerField(default=999)

    def __str__(self):
        return self.ismi

    class Meta:
        db_table = 'Registr'

    def is_valid(self):
        pass
class Tugarak(models.Model):
    image=models.ImageField(upload_to="images/")
    subjects=models.CharField(max_length=200, verbose_name="nomi")
    body_small=models.TextField()
    body=models.TextField()
    muallimi=models.CharField(max_length=200)
    muallim_name=models.CharField(max_length=200)
    publish_time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nomi
    class Meta:
        db_table = 'To\'garak'
        verbose_name = 'To\'garak'


# Create your models here.
