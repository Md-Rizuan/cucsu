from django.db import models

# Create your models here.
# elections/models.py

POSITION_CHOICES = [
    ('president', 'সভাপতি'),
    ('vp', 'ভিপি'),
    ('gs', 'জিএস'),
    ('ags', 'এজিএস'),
    ('treasurer', 'কোষাধ্যক্ষ'),
    ('sports', 'খেলাধুলা ও ক্রীড়া সম্পাদক'),
    ('asst_sports', 'সহ খেলাধুলা ও ক্রীড়া সম্পাদক'),
    ('culture', 'সাহিত্য-সংস্কৃতি সম্পাদক'),
    ('asst_culture', 'সহ সাহিত্য-সংস্কৃতি সম্পাদক'),
    ('office', 'দপ্তর সম্পাদক'),
    ('asst_office', 'সহ-দপ্তর সম্পাদক'),
    ('welfare', 'ছাত্রী কল্যাণ সম্পাদক'),
    ('asst_welfare', 'সহ-ছাত্রী কল্যান সম্পাদক'),
    ('social_env', 'সমাজসেবা ও পরিবেশ বিষয়ক সম্পাদক'),
    ('law_hr', 'আইন ও মানবাধিকার বিষয়ক সম্পাদক'),
    ('freedom', 'মুক্তিযুদ্ধ ও গণতান্ত্রিক আন্দোলন বিষয়ক সম্পাদক'),
    ('career', 'ক্যারিয়ার ডেভেলপমেন্ট ও আন্তর্জাতিক বিষয়ক সম্পাদক'),
    ('communication', 'যোগাযোগ ও আবাসন সম্পাদক'),
    ('asst_communication', 'সহ-যোগাযোগ ও আবাসন সম্পাদক'),
    ('research', 'গবেষণা ও উদ্ভাবন সম্পাদক'),
    ('science_it', 'বিজ্ঞান ও তথ্যপ্রযুক্তি সম্পাদক'),
    ('health', 'স্বাস্থ্য সম্পাদক'),
    ('library_cafe', 'পাঠাগার ও ক্যাফেটেরিয়া বিষয়ক সম্পাদক'),
    ('executive', 'নির্বাহী সদস্য'),
]

class Candidate(models.Model):
  

    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    session = models.CharField(max_length=50)
    student_id = models.CharField(max_length=20)
    image = models.ImageField(upload_to='candidates/')
    manifesto = models.TextField()
    position = models.CharField(max_length=100, choices=POSITION_CHOICES)
    ballot = models.CharField(max_length=50)
    panel = models.CharField(max_length=50)

    def __str__(self):
        return self.name
