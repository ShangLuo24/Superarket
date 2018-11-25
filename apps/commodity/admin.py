from django.contrib import admin
from commodity.models import Class, Goods, Unti, Create, PhotoAlbum, SlideShow, Home, Activity, Division


class ClassInline(admin.StackedInline):
    model = Goods  # 该处配置多端表
    extra = 1


class UntiInline(admin.StackedInline):
    model = Goods  # 该处配置多端表
    extra = 1


class CreateInline(admin.StackedInline):
    model = Goods  # 该处配置多端表
    extra = 1


class PhotoAlbumInline(admin.StackedInline):
    model = PhotoAlbum  # 该处配置多端表
    extra = 1


class SlideShowInline(admin.StackedInline):
    model = SlideShow  # 该处配置多端表
    extra = 1


class DivisionInline(admin.StackedInline):
    model = Division  # 该处配置多端表
    extra = 1


class GoodsInline(admin.StackedInline):
    model = Goods
    extra = 1


# 商品分类表格
@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    #  每页显示多少项
    list_per_page = 5

    # 设置显示字段
    #  更改名字默认值.verbose_name='上级区域'
    list_display = ['id', 'class_name', 'class_intro']

    # 在字段上添加一个连接, 能点进去编辑
    list_display_links = ['id', 'class_name', 'class_intro']

    # 过滤器
    list_filter = ['class_name']

    # 添加搜索框
    search_fields = ['class_name']

    # 编辑或者添加的字段
    fields = ['class_name', 'class_intro']

    # 将多端配置添加到管理界面
    inlines = [
        ClassInline
    ]


# 商品 SKU 表
@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    #  每页显示多少项
    list_per_page = 5

    # 设置显示字段
    list_display = ['id',
                    'Goods_sku_name',
                    'Goods_sku_intro',
                    'Goods_sku_Is_putaway',
                    'Goods_sku_cate_id',
                    'Goods_spu_id'
                    ]

    # 在字段上添加一个连接, 能点进去编辑
    list_display_links = ['id',
                          'Goods_sku_name',
                          'Goods_sku_intro',
                          ]

    # 过滤器
    list_filter = ['Goods_sku_name']

    # 添加搜索框
    search_fields = ['Goods_sku_name']

    # 编辑或者添加的字段
    fields = ['Goods_sku_name',
              'Goods_sku_intro',
              'Goods_sku_Price',
              'Goods_sku_Unitinfo',
              'Goods_sku_Num',
              'Goods_sku_Sellnum',
              'Goods_sku_Logo',
              'Goods_sku_Is_putaway',
              'Goods_sku_cate_id',
              'Goods_spu_id',
              ]

    # 将多端配置添加到管理界面
    inlines = [
        PhotoAlbumInline,
        SlideShowInline,
        DivisionInline,
    ]


# 商品单位表
@admin.register(Unti)
class UntiAdmin(admin.ModelAdmin):
    #  每页显示多少项
    list_per_page = 5

    # 设置显示字段
    list_display = ['id', 'class_unit']

    # 在字段上添加一个连接, 能点进去编辑
    list_display_links = ['id', 'class_unit']

    # 过滤器
    list_filter = ['class_unit']

    # 添加搜索框
    search_fields = ['class_unit']

    # 编辑或者添加的字段
    fields = ['class_unit']

    # 将多端配置添加到管理界面
    inlines = [
        UntiInline
    ]


# 商品 SPU 表
@admin.register(Create)
class CreateAdmin(admin.ModelAdmin):
    #  每页显示多少项
    list_per_page = 5

    # 设置显示字段
    list_display = ['id', 'Goods_spu_name', 'Goods_spu_intro']

    # 在字段上添加一个连接, 能点进去编辑
    list_display_links = ['id', 'Goods_spu_name']

    # 过滤器
    list_filter = ['Goods_spu_name']

    # 添加搜索框
    search_fields = ['Goods_spu_name']

    # 编辑或者添加的字段
    fields = ['Goods_spu_name',
              'Goods_spu_intro',
              ]

    # 将多端配置添加到管理界面
    inlines = [
        CreateInline
    ]


# 商品相册
@admin.register(PhotoAlbum)
class PhotoAlbumAdmin(admin.ModelAdmin):
    #  每页显示多少项
    list_per_page = 5

    # 设置显示字段
    list_display = ['id', 'Goods_Img_url']

    # 在字段上添加一个连接, 能点进去编辑
    list_display_links = ['id', 'Goods_Img_url']

    # 过滤器
    list_filter = ['Goods_Img_url']

    # # 添加搜索框
    # search_fields = ['Goods_Img_url']

    # 编辑或者添加的字段
    fields = ['Goods_Img_url',
              ]


# 首页模块
@admin.register(SlideShow)
class SlideShowAdmin(admin.ModelAdmin):
    #  每页显示多少项
    list_per_page = 5

    # 设置显示字段
    list_display = ['id', 'Page_name', 'Goods_sku_id', 'Page_Order']

    # 在字段上添加一个连接, 能点进去编辑
    list_display_links = ['id', 'Page_name']

    # 过滤器
    list_filter = ['Page_name']

    # # 添加搜索框
    search_fields = ['Page_name']

    # 编辑或者添加的字段
    fields = ['Page_name',
              'Goods_sku_id',
              'Page_Imgurl',
              'Page_Order',
              ]


# 首页活动表
@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    #  每页显示多少项
    list_per_page = 5

    # 设置显示字段
    list_display = ['id', 'Home_name', 'Home_Linkurl']

    # 在字段上添加一个连接, 能点进去编辑
    list_display_links = ['id', 'Home_name']

    # 过滤器
    list_filter = ['Home_name']

    # # 添加搜索框
    search_fields = ['Home_name', 'Home_Linkurl']

    # 编辑或者添加的字段
    fields = ['Home_name',
              'Home_Imgurl',
              'Home_Linkurl',
              ]


# 首页活动专区
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    #  每页显示多少项
    list_per_page = 5

    # 设置显示字段
    list_display = ['id', 'Activity', 'Activity_Describe', 'Activity_Order', 'Activity_on_putaway']

    # 在字段上添加一个连接, 能点进去编辑
    list_display_links = ['id', 'Activity']

    # 过滤器
    list_filter = ['Activity']

    # # 添加搜索框
    search_fields = ['Activity', 'Activity_Describe']

    # 编辑或者添加的字段
    fields = ['Activity',
              'Activity_Describe',
              'Activity_Order',
              'Activity_on_putaway',
              ]

    inlines = [
        DivisionInline
    ]


# 首页专区活动商品表
@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    #  每页显示多少项
    list_per_page = 5

    # 设置显示字段
    list_display = ['id', 'Division', 'Division_sku']

    # 在字段上添加一个连接, 能点进去编辑
    list_display_links = ['id', 'Division', 'Division_sku']

    # 过滤器
    list_filter = ['Division']

    # # 添加搜索框
    search_fields = ['Division', 'Division_sku']

    # 编辑或者添加的字段
    fields = ['Division',
              'Division_sku',
              ]

    # inlines = [
    #     GoodsInline
    # ]