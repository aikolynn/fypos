# #coding=utf-8
from django.db import models
#
# # Create your models here.
# class PosTSaleman(models.Model):
#     sale_id = models.CharField(max_length=4,verbose_name='序号',primary_key=True)
#     sale_name = models.CharField(max_length=10,verbose_name='姓名')
#     sale_status = models.CharField(max_length=4,verbose_name='状态')
#     memo = models.CharField(max_length=20, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'pos_t_saleman'
#     def __unicode__(self):
#         return self.sale_name
#
# class PosVipInfo(models.Model):
#     vip_id = models.CharField(max_length=20,verbose_name='会员卡号',primary_key=True)
#     vip_name = models.CharField(max_length=8, blank=True, null=True,verbose_name='会员')
#     vip_sex = models.CharField(max_length=2, blank=True, null=True,verbose_name='性别')
#     vip_tel = models.CharField(max_length=16, blank=True, null=True,verbose_name='电话')
#     vip_mbl = models.CharField(max_length=16, blank=True, null=True,verbose_name='手机')
#     shop = models.CharField(max_length=10, blank=True, null=True,verbose_name='门店')
#
#     class Meta:
#         verbose_name='会员'
#         verbose_name_plural=verbose_name
#         managed = False
#         db_table = 'pos_vip_info'
#     def __unicode__(self):
#         return  self.vip_name
#
#
# class SaleFlow(models.Model):
#     id = models.FloatField(db_column='ID', blank=True,primary_key=True)  # Field name made lowercase.
#     shop = models.CharField(db_column='SHOP', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     sale_id = models.FloatField(db_column='SALE_ID', blank=True, null=True)  # Field name made lowercase.
#     item_no = models.CharField(db_column='ITEM_NO', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     item_name = models.CharField(db_column='ITEM_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     sale_price = models.FloatField(db_column='SALE_PRICE', blank=True, null=True)  # Field name made lowercase.
#     discount = models.FloatField(db_column='Discount', blank=True, null=True)  # Field name made lowercase.
#     sale_count = models.FloatField(db_column='SALE_COUNT', blank=True, null=True)  # Field name made lowercase.
#     amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
#     sale_way_id = models.CharField(db_column='Sale_way_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     sale_way = models.CharField(db_column='Sale_way', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     saler_id = models.CharField(db_column='Saler_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     saler = models.CharField(db_column='Saler', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     sale_time = models.DateTimeField(db_column='Sale_Time', blank=True, null=True)  # Field name made lowercase.
#     cls_name = models.CharField(max_length=20, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sale_flow'
#
#
# class SaleFlowBack(models.Model):
#     id = models.FloatField(db_column='ID', blank=True, primary_key=True)  # Field name made lowercase.
#     shop = models.CharField(db_column='SHOP', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     sale_id = models.FloatField(db_column='SALE_ID', blank=True, null=True)  # Field name made lowercase.
#     item_no = models.CharField(db_column='ITEM_NO', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     item_name = models.CharField(db_column='ITEM_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     sale_price = models.FloatField(db_column='SALE_PRICE', blank=True, null=True)  # Field name made lowercase.
#     discount = models.FloatField(db_column='Discount', blank=True, null=True)  # Field name made lowercase.
#     sale_count = models.FloatField(db_column='SALE_COUNT', blank=True, null=True)  # Field name made lowercase.
#     amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
#     sale_way_id = models.CharField(db_column='Sale_way_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     sale_way = models.CharField(db_column='Sale_way', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     saler_id = models.CharField(db_column='Saler_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     saler = models.CharField(db_column='Saler', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     sale_time = models.DateTimeField(db_column='Sale_Time', blank=True, null=True)  # Field name made lowercase.
#     cls_name = models.CharField(max_length=20, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sale_flow_back'
#
#
# class SaleFlowLaster(models.Model):
#     id = models.FloatField(db_column='ID', blank=True,verbose_name='ID',primary_key=True)  # Field name made lowercase.
#     shop = models.CharField(db_column='SHOP', max_length=255, blank=True, null=True,verbose_name='门店')  # Field name made lowercase.
#     sale_id = models.FloatField(db_column='SALE_ID', blank=True, null=True,verbose_name='销售小票号')  # Field name made lowercase.
#     item_no = models.CharField(db_column='ITEM_NO', max_length=255, blank=True, null=True,verbose_name='商品编码')  # Field name made lowercase.
#     item_name = models.CharField(db_column='ITEM_NAME', max_length=255, blank=True, null=True,verbose_name='商品名称')  # Field name made lowercase.
#     sale_price = models.FloatField(db_column='SALE_PRICE', blank=True, null=True,verbose_name='销售价')  # Field name made lowercase.
#     discount = models.FloatField(db_column='Discount', blank=True, null=True,verbose_name='折扣价')  # Field name made lowercase.
#     sale_count = models.FloatField(db_column='SALE_COUNT', blank=True, null=True,verbose_name='销售额')  # Field name made lowercase.
#     amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
#     sale_way_id = models.CharField(db_column='Sale_way_ID', max_length=255, blank=True, null=True,verbose_name='销售方式ID')  # Field name made lowercase.
#     sale_way = models.CharField(db_column='Sale_way', max_length=255, blank=True, null=True,verbose_name='销售方式')  # Field name made lowercase.
#     saler_id = models.CharField(db_column='Saler_ID', max_length=255, blank=True, null=True,verbose_name='销售员ID')  # Field name made lowercase.
#     saler = models.CharField(db_column='Saler', max_length=255, blank=True, null=True,verbose_name='销售员')  # Field name made lowercase.
#     sale_time = models.DateTimeField(db_column='Sale_Time', blank=True, null=True)  # Field name made lowercase.
#     cls_name = models.CharField(max_length=20, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sale_flow_laster'