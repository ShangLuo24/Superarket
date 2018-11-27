from django.contrib import admin

# 商品分类表格
from orderForm.models import DeliveryAddress, Payment, OrderInformation, OrdersGoods, TypeShipping


class OrderInformationInline(admin.StackedInline):
    model = OrderInformation  # 该处配置多端表
    extra = 1


class OrdersGoodsInline(admin.StackedInline):
    model = OrdersGoods  # 该处配置多端表
    extra = 1


@admin.register(DeliveryAddress)
class DeliveryAddressAdmin(admin.ModelAdmin):
    #  每页显示多少项
    list_per_page = 5

    # 设置显示字段
    list_display = ['id', 'userName', 'telephone', "default"]

    # 在字段上添加一个连接, 能点进去编辑
    list_display_links = ['id', 'userName', 'telephone']

    # 过滤器
    list_filter = ['userName']

    # 添加搜索框
    search_fields = ['userName']

    # 编辑或者添加的字段
    fields = ['userName',
              'telephone',
              'province',
              'city',
              'district',
              'street',
              'inDetail',
              'default',
              ]

    inlines = [
        OrderInformationInline
    ]


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    #  每页显示多少项
    list_per_page = 5

    # 设置显示字段
    list_display = ['id', 'pay', 'payImg']

    # 在字段上添加一个连接, 能点进去编辑
    list_display_links = ['id', 'pay', 'payImg']

    # 过滤器
    list_filter = ['pay']

    # 添加搜索框
    search_fields = ['pay']

    # 编辑或者添加的字段
    fields = ['pay',
              'payImg'
              ]

    inlines = [
        OrderInformationInline
    ]


@admin.register(OrderInformation)
class OrderInformationAdmin(admin.ModelAdmin):
    #  每页显示多少项
    list_per_page = 5

    # 设置显示字段
    list_display = ['id', 'orderNum', 'orderPrice', 'UserName', 'orderState', 'transitKey', 'PaymentKey']

    # 在字段上添加一个连接, 能点进去编辑
    list_display_links = ['id', 'orderNum', 'orderPrice', 'UserName', 'orderState', 'transitKey', 'PaymentKey']

    # 过滤器
    list_filter = ['orderNum']

    # 添加搜索框
    search_fields = ['orderNum']

    # 编辑或者添加的字段
    fields = ['orderNum',
              'orderPrice',
              'UserKey',
              'UserName',
              'Telephone',
              'AddressKey',
              'orderState',
              'transitKey',
              'PaymentKey',
              'money',
              ]

    inlines = [
        OrdersGoodsInline
    ]


@admin.register(OrdersGoods)
class OrdersGoodsAdmin(admin.ModelAdmin):
    #  每页显示多少项
    list_per_page = 5

    # 设置显示字段
    list_display = ['id', 'OrderInformation', 'goodsSku', 'goodsNum', 'goodsPrice']

    # 在字段上添加一个连接, 能点进去编辑
    list_display_links = ['id', 'OrderInformation', 'goodsSku', 'goodsNum', 'goodsPrice']

    # 过滤器
    list_filter = ['OrderInformation']

    # 添加搜索框
    search_fields = ['OrderInformation']

    # 编辑或者添加的字段
    fields = ['OrderInformation',
              'goodsSku',
              'goodsNum',
              'goodsPrice'
              ]


@admin.register(TypeShipping)
class TypeShippingAdmin(admin.ModelAdmin):
    #  每页显示多少项
    list_per_page = 5

    # 设置显示字段
    list_display = ['id', 'transit', 'transitCharge']

    # 在字段上添加一个连接, 能点进去编辑
    list_display_links = ['id', 'transit', 'transitCharge']

    # 过滤器
    list_filter = ['transit']

    # 添加搜索框
    search_fields = ['transit']

    # 编辑或者添加的字段
    fields = ['transit',
              'transitCharge'
              ]

    inlines = [
        OrderInformationInline
    ]
