from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from Superarket import settings
from db.base_model import BaseModel


# 商品分类表格
class Class(BaseModel):
    """
    商品分类:
    分类名
    分类简介
    添加时间
    修改时间
    是否删除
    """
    class_name = models.CharField(max_length=50, verbose_name='商品分类名')
    class_intro = models.CharField(max_length=255, verbose_name="分类简介")

    class Meta:
        db_table = "Class"
        verbose_name = '商品分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.class_name


# 商品单位表
class Unti(BaseModel):
    """
    商品单位表:
    商品名称
    添加时间
    修改时间
    是否删除
    """
    class_unit = models.CharField(max_length=50, verbose_name='单位名称')

    class Meta:
        db_table = "Unti"
        verbose_name = '商品单位表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.class_unit


# 商品 SKU 表
class Goods(BaseModel):
    """

    """
    Is_putaway_choices = (
        (1, '上架'),
        (2, '未上架'),
    )
    Goods_sku_name = models.CharField(max_length=50, verbose_name='商品信息')
    Goods_sku_intro = RichTextUploadingField(verbose_name='商品简介')
    Goods_sku_Price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='商品价格', default=0)
    Goods_sku_Unitinfo = models.ForeignKey(to="Unti", on_delete=models.CASCADE, verbose_name='单位')
    Goods_sku_Num = models.IntegerField(verbose_name='库存')
    Goods_sku_Sellnum = models.IntegerField(verbose_name='销售量', default=0)
    Goods_sku_Logo = models.ImageField(upload_to='Goods/%Y%m/%d', verbose_name='logo图片')
    Goods_sku_Is_putaway = models.SmallIntegerField(choices=Is_putaway_choices, default=1, verbose_name='上架')
    Goods_sku_cate_id = models.ForeignKey(to="Class", on_delete=models.CASCADE, verbose_name='商品分类id')
    Goods_spu_id = models.ForeignKey(to="Create", on_delete=models.CASCADE, verbose_name='商品spu_id')

    def show_logo(self):
        return "<img src='{}{}'/>".format(settings.MEDIA_URL, self.Goods_sku_Logo)

    show_logo.allow_tags = True
    show_logo.short_description = 'Goods_sku_Logo'

    class Meta:
        db_table = "Goods"
        verbose_name = '商品sku表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Goods_sku_name


# 商品 SPU 表
class Create(BaseModel):
    """
    商品 SPU 表:
    名称
    详情
    """
    Goods_spu_name = models.CharField(max_length=50, verbose_name='商品名称')
    Goods_spu_intro = RichTextUploadingField(verbose_name='商品详情')

    class Meta:
        db_table = "Create"
        verbose_name = '商品spu表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Goods_spu_name


# 商品相册
class PhotoAlbum(BaseModel):
    """
    商品相册:
    图片地址
    商品SKU_ID
    """
    Goods_Img_url = models.ImageField(upload_to='PhotoAlbum/%Y%m/%d', verbose_name='图片地址')
    Class = models.ForeignKey(to='Goods', on_delete=models.CASCADE)

    class Meta:
        db_table = "PhotoAlbum"
        verbose_name = '商品相册'
        verbose_name_plural = verbose_name


# 首页模块
class SlideShow(BaseModel):
    """
    首页轮播商品
    名称
    商品sku_id
    图片地址
    排序
    """
    Page_name = models.CharField(max_length=50, verbose_name="轮播图名称")
    Goods_sku_id = models.ForeignKey(to='Goods', on_delete=models.CASCADE, verbose_name='商品SKUid')
    Page_Imgurl = models.ImageField(upload_to='show/%Y%m/%d', verbose_name='图片地址')
    Page_Order = models.SmallIntegerField(verbose_name="排序", default=0)

    class Meta:
        db_table = "SlideShow"
        verbose_name = '首页模块'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Page_name


# 首页活动表
class Home(BaseModel):
    """
    首页活动表
    首页名字
    图片地址
    url地址 默认www.jd.com
    """
    Home_name = models.CharField(max_length=50, verbose_name="首页名字")
    Home_Imgurl = models.ImageField(upload_to='Home/%Y%m/%d', verbose_name='图片地址')
    Home_Linkurl = models.URLField(max_length=50, verbose_name="url地址")

    class Meta:
        db_table = "Home"
        verbose_name = '首页活动表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Home_name


# 首页活动专区
class Activity(BaseModel):
    """
    首页活动专区
    首页活动名字
    描述
    排序
    时候上架
    """
    Is_putaway = (
        (1, '上架'),
        (0, '未上架'),
    )
    Activity = models.CharField(max_length=50, verbose_name="首页活动名字")
    Activity_Describe = models.CharField(max_length=255, verbose_name="首页活动描述")
    Activity_Order = models.SmallIntegerField(verbose_name="排序", default=0)
    Activity_on_putaway = models.BooleanField(choices=Is_putaway, default=1, verbose_name="是否上架")

    class Meta:
        db_table = "Activity"
        verbose_name = '首页活动专区'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Activity


# 首页专区活动商品表
class Division(BaseModel):
    """
    首页专区活动商品表
    专区id
    商品sku_id
    """
    Division = models.ForeignKey(to='Activity', on_delete=models.CASCADE, verbose_name='专区id')
    Division_sku = models.ForeignKey(to='Goods', on_delete=models.CASCADE, verbose_name='商品SKUid')

    class Meta:
        db_table = "Division"
        verbose_name = '首页专区活动商品表'
        verbose_name_plural = verbose_name
