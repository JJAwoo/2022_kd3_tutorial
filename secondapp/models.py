from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=30, verbose_name='이름')
    cnt =  models.IntegerField()    

class ArmyShop(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    type = models.TextField()
    name = models.TextField()
    # meta 를 주지 않으면 secondapp_army_shop 테이블이 만들어짐?

    class Meta:

        # 테이블명을 army_shop으로 지정
        db_table = 'army_shop'
        
        # migration 대상 여부
        managed = False

