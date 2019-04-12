from django.db import models


# 1.1 用Django建国家信息模型Country, 属性： 国家名称，国家url连接地址， 用drf完成国家信息创建和列表展示接口
class Country(models.Model):
    c_name = models.CharField(max_length=255)
    c_href = models.CharField(max_length=255)

    class Meta:
        db_table = 'country'


# 2.1 用Django建  酒分页信息模型WinePage, 属性： 分页url， 与国家信息模型 外键关联,  用drf完成 酒分页信息创建和列表展示接口
class WinePage(models.Model):
    w_href = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='winepage')

    class Meta:
        db_table = 'winepage'


# 3.1 用Django建  酒信息模型 WineInfo,  与 WinePage模型 外键关联, 用drf完成 酒信息创建和列表展示接口
# 要爬取的酒类信息如下:  国家和产区, 国际均价ex-tax,  生产商,  品种, 获奖,  其他亮点评述:
class WineInfo(models.Model):
    region = models.CharField(max_length=255)
    ex_tax = models.CharField(max_length=255)
    producer = models.CharField(max_length=255)
    grape = models.CharField(max_length=255)
    awards = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    winepage = models.ForeignKey(WinePage, on_delete=models.CASCADE, related_name='wineinfo')

    class Meta:
        db_table = 'wineinfo'
