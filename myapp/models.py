# from django.db import models

from djongo import models
import json

from django.contrib.auth.models import AbstractBaseUser,AbstractUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


# Create your models here.


class UserModel(models.Model):
    username=models.TextField()
    age=models.IntegerField()
    mark=models.FloatField()
    def __str__(self):
        return self.username

class Student(models.Model):
    
    name=models.TextField()
    date=models.DateTimeField()
    dob=models.DateTimeField()
    mobileNumber=models.TextField()
    address=models.TextField()
    qualification=models.TextField()
    nationality=models.TextField()
    workingDesignation=models.TextField()
    studentCollegeName=models.TextField()
    email=models.EmailField()
    whatsappNumber=models.TextField()
    gender=models.TextField()

   
    def __str__(self):
        return self.name
    
# class CustomUserManager(BaseUserManager):
#     def create_user(self, oceanRegisterNo,email, password=None,**extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(oceanRegisterNo=oceanRegisterNo, email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self,oceanRegisterNo, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(oceanRegisterNo,email, password, **extra_fields)


class CustomUserManager(BaseUserManager):
    def create_user(self, oceanRegisterNo, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(oceanRegisterNo=oceanRegisterNo, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, oceanRegisterNo,email, password=None, **extra_fields):
        # Ensure that the email field is set and normalize it
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        # Call the base class create_superuser method
        user = self.create_user(oceanRegisterNo, email, password, **extra_fields)
        # Additional superuser-specific fields can be set here if needed
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
        # extra_fields.setdefault('is_staff', True)
        # extra_fields.setdefault('is_superuser', True)
        # # Call the base class create_superuser method
        # return super().create_superuser( email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    studentName = models.TextField()
    oceanRegisterNo=models.TextField(unique=True)
    mobileNumber = models.TextField()
    email = models.EmailField()
    password=models.TextField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'oceanRegisterNo'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.oceanRegisterNo

class McqListDatatModel(models.Model):
    id = models.IntegerField(primary_key=True)  # or models.AutoField(primary_key=True)
    mcqName = models.TextField()
    def save(self, *args, **kwargs):
        if not self.id:
            # Fetch the last used id and increment it
            last_used_id = McqListDatatModel.objects.order_by('-id').first()
            self.id = last_used_id.id + 1 if last_used_id else 1

        super().save(*args, **kwargs)

    def __str__(self):
        return self.mcqName
    

class LanguageModel(models.Model):
    mcqId = models.ForeignKey(McqListDatatModel, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    languageName = models.TextField()

    def save(self, *args, **kwargs):
        if not self.id:
            # Fetch the last used id and increment it
            last_used_id = LanguageModel.objects.order_by('-id').first()
            self.id = last_used_id.id + 1 if last_used_id else 1

        super().save(*args, **kwargs)

    def __str__(self):
        return self.languageName
# class LanguageModel(models.Model):
#     mcqId=models.ForeignKey(McqListDatatModel,on_delete=models.CASCADE)
#     languageName=models.TextField()
#     def __str__(self):
#         return self.languageName
    
# class TopicModel(models.Model):
#     languageId=models.ForeignKey(LanguageModel, on_delete=models.CASCADE)
#     topicName=models.TextField()
#     def __str__(self):
#         return self.topicName

class TopicModel(models.Model):
    languageId = models.ForeignKey(LanguageModel, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    topicName = models.TextField()

    def save(self, *args, **kwargs):
        if not self.id:
            # Fetch the last used id and increment it
            last_used_id = TopicModel.objects.order_by('-id').first()
            self.id = last_used_id.id + 1 if last_used_id else 1

        super().save(*args, **kwargs)

    def __str__(self):
        return self.topicName
        
# class QuestionModel(models.Model):
#     languageId=models.ForeignKey(LanguageModel, on_delete=models.CASCADE)
#     topicId=models.ForeignKey(TopicModel,on_delete=models.CASCADE)
#     questions=models.JSONField()
#     level=models.TextField()
#     mark=models.IntegerField()
#     time=models.IntegerField()
#     def get_questions_as_dict(self):
#         return json.loads(self.questions)

class QuestionModel(models.Model):
    languageId = models.ForeignKey(LanguageModel, on_delete=models.CASCADE)
    topicId = models.ForeignKey(TopicModel, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    questions = models.JSONField()
    level = models.TextField()
    mark = models.IntegerField()
    time = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.id:
            # Fetch the last used id and increment it
            last_used_id = QuestionModel.objects.order_by('-id').first()
            self.id = last_used_id.id + 1 if last_used_id else 1

        super().save(*args, **kwargs)

    def get_questions_as_dict(self):
        return json.loads(self.questions)
    
# class ResultModel(models.Model):
#     userID=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     languageId=models.ForeignKey(LanguageModel, on_delete=models.CASCADE)
#     topicId=models.ForeignKey(TopicModel,on_delete=models.CASCADE)
#     answeredQuestions=models.JSONField()
#     result=models.IntegerField()
#     level=models.TextField()

class ResultModel(models.Model):
    userID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    languageId = models.ForeignKey(LanguageModel, on_delete=models.CASCADE)
    topicId = models.ForeignKey(TopicModel, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    answeredQuestions = models.JSONField()
    result = models.IntegerField()
    level = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.created_at = timezone.now().astimezone(timezone.pytz.timezone('Asia/Kolkata'))
        if not self.id:
            # Fetch the last used id and increment it
            last_used_id = ResultModel.objects.order_by('-id').first()
            self.id = last_used_id.id + 1 if last_used_id else 1

        super().save(*args, **kwargs)


class LeaderBoardModel(models.Model):
    userID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    username=models.TextField()
    result=models.IntegerField()
    noOfTestAttended=models.IntegerField()
