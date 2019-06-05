from django.db import models


# 内网地址, wanip 一对多对应外网地址表
class Laninter(models.Model):
    lanip = models.GenericIPAddressField()

    def __str__(self):
        return self.lanip

# 外网地址
class Waninter(models.Model):
    wanip = models.GenericIPAddressField(unique=True)

    def __str__(self):
        return self.wanip

# 关系映射表， 映射对照于内网
class Mapping(models.Model):
    '''
        mapid: 用于对应防火墙映射关系的ID值，不能为自增
        serid: 序列号ID, 用于映射之间的序列号， 都是整形, 不能带小数点
        chiose： 固定死的格式就不在用数据库
        protocol: 协议: tcp, udp, icmp
    '''
    mapid = models.PositiveIntegerField()
    serid = models.PositiveIntegerField()
    chiose = ((1, "tcp"), (2, "udp"), (3, "icmp"))
    protocol = models.IntegerField(choices=chiose, default=1)
    lanport = models.PositiveIntegerField()
    wanport = models.PositiveIntegerField()
    lanip = models.ForeignKey(to='Laninter', on_delete=models.CASCADE)
    wanip = models.ForeignKey(to='Waninter', to_field='id', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('lanip', 'lanport', 'wanport')
