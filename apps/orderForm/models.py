from django.db import models
from commodity.models import Goods
from db.base_model import BaseModel
from user.models import Username


class DeliveryAddress(BaseModel):
    # 收货地址
    """
    用户ID
    收货人姓名
    手机号码
    省ID
    市ID
    区ID
    街道ID
    详细描述
    是否是默认地址
    """
    # Is_default = (
    #     (1, '默认'),
    #     (0, '不默认'),
    # )
    user = models.ForeignKey(to=Username, verbose_name='用户id')
    userName = models.CharField(max_length=50, verbose_name='收货人姓名')
    telephone = models.CharField(max_length=11, verbose_name='电话号码')
    harea = models.CharField(max_length=50, null=True, blank=True, verbose_name='省')
    hproper = models.CharField(max_length=50, null=True, blank=True, verbose_name='市')
    hcity = models.CharField(max_length=50, verbose_name='区')
    street = models.CharField(max_length=50, verbose_name='街道')
    inDetail = models.CharField(max_length=255, verbose_name='详细描述')
    default = models.BooleanField(default=False, verbose_name="默认地址")

    def __str__(self):
        return self.userName

    class Meta:
        db_table = "DeliveryAddress"
        verbose_name = '收货地址'
        verbose_name_plural = verbose_name


class Payment(BaseModel):
    # 付款方式
    """
    付款名称
    结账图片
    """
    pay = models.CharField(max_length=50, verbose_name='付款名称')
    payImg = models.ImageField(upload_to='Home/%Y%m/%d', verbose_name='支付图片')

    class Meta:
        db_table = "payment"
        verbose_name = '付款方式'
        verbose_name_plural = verbose_name


class OrderInformation(BaseModel):
    # 订单信息
    """
    订单编号
    订单金额
    用户ID
    收货人姓名
    收货人电话
    收货id
    订单状态
    运输id
    付款id
    实付金额
    """
    State = {
        (0, '待付款'),
        (1, '退发货'),
        (2, '待收货'),
        (3, '待评价'),
        (4, '已完成'),
    }
    orderNum = models.CharField(max_length=50, verbose_name='订单编号', unique=True)
    orderPrice = models.DecimalField(max_digits=9, decimal_places=2, default=0, verbose_name='订单价格')
    UserKey = models.ForeignKey(to=Username, verbose_name='用户ID')
    UserName = models.CharField(max_length=50, verbose_name='收货人姓名')
    Telephone = models.CharField(max_length=11, verbose_name='收货人电话')
    AddressKey = models.ForeignKey(to='DeliveryAddress', on_delete=models.CASCADE, verbose_name='收货地址')
    orderState = models.SmallIntegerField(choices=State, default=0, verbose_name='订单状态')
    transitKey = models.CharField(max_length=50, verbose_name='运输方式')
    transit_price_Key = models.DecimalField(max_digits=9, decimal_places=2, default=0, verbose_name='运输价格')
    PaymentKey = models.ForeignKey(to="Payment", on_delete=models.CASCADE, null=True, blank=True, verbose_name='付款方式')
    money = models.DecimalField(max_digits=9, decimal_places=2, default=0, verbose_name='实际支付')

    class Meta:
        db_table = "OrderInformation"
        verbose_name = '订单信息'
        verbose_name_plural = verbose_name


class OrdersGoods(BaseModel):
    # 订单商品
    """
    订单ID
    商品SKU ID
    商品数量
    商品价格
    """
    OrderInformation = models.ForeignKey(to="OrderInformation", on_delete=models.CASCADE, verbose_name='订单信息')
    goodsSku = models.ForeignKey(to=Goods, on_delete=models.CASCADE, verbose_name='SKU商品')
    goodsNum = models.SmallIntegerField(verbose_name='商品数量')
    goodsPrice = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='商品价格')

    class Meta:
        db_table = "OrdersGoods"
        verbose_name = '订单商品'
        verbose_name_plural = verbose_name


class TypeShipping(BaseModel):
    # 运输方式
    """
    ID
    名称
    价格
    """
    transit = models.CharField(max_length=50, verbose_name='运输名称')
    transitCharge = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='运输价格', default=0)

    class Meta:
        db_table = "TypeShipping"
        verbose_name = '运输方式'
        verbose_name_plural = verbose_name
