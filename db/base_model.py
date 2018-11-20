from django.db import models


class BaseModel(models.Model):
    """
    这三个参数属于公共部分,让models.py去继承这里,那么就可以减少代码量
    """
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name="创建时间",
                                       )
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name="更新时间",
                                       )
    is_delete = models.BooleanField(default=False,
                                    verbose_name="是否删除",
                                    )

    class Meta:
        # 说明是抽象模型类，不会被迁移
        abstract = True
