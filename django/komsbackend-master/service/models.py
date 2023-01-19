from django.db import models

# All KOMS model here.

class Order_point(models.Model):
    name = models.CharField(max_length=50)
    activation_status = models.BooleanField(default=False)

class Order_point_cred(models.Model):
    pointId = models.ForeignKey(Order_point, on_delete=models.CASCADE)
    key     = models.CharField(max_length=100)
    value   = models.CharField(max_length=500)


class Stations(models.Model):
    station_name    = models.CharField(max_length=50)
    client_id       = models.CharField(max_length=200)
    client_secrete  = models.CharField(max_length=200)
    tag             = models.CharField(max_length=20)
    color_code      = models.CharField(max_length=10,default=0xFF2E2E48)
    isStation       = models.BooleanField(default=True)

class Order(models.Model):
    externalOrderId = models.IntegerField()
    pickupTime      = models.CharField(max_length=90)
    deliveryIsAsap  = models.BooleanField(default=False)
    order_point     = models.ForeignKey(Order_point, on_delete=models.CASCADE,null=True,default=1)
    # arrival_time    = models.CharField(max_length=90)
    arrival_time    = models.DateTimeField(auto_now=True)
    estimated_time  = models.CharField(max_length=30)
    order_status    = models.IntegerField()
    order_note      = models.CharField(max_length=100)
    order_type      = models.IntegerField()
    itemRemark      = models.CharField(max_length=40, default='')

class Original_order(models.Model):
    orderId         = models.ForeignKey(Order, on_delete=models.CASCADE)
    OrderJSON       = models.CharField(max_length=1000)
    update_time     = models.CharField(max_length=20)
    externalOrderId = models.CharField(max_length=30)
    parent          = models.CharField(max_length=30)

class Order_content(models.Model):
    orderId         = models.ForeignKey(Order, on_delete=models.CASCADE)
    name            = models.CharField(max_length=50)
    quantity        = models.IntegerField()
    stationName     = models.CharField(max_length=50)
    quantityStatus  = models.IntegerField()
    unit            = models.CharField(max_length=20)
    note            = models.CharField(max_length=50)
    SKU             = models.CharField(max_length=30)
    tag             = models.CharField(max_length=30)
    stationId       = models.ForeignKey(Stations, on_delete=models.CASCADE)
    status          = models.CharField(max_length=30)

class Order_modifer(models.Model):
    contentID       = models.ForeignKey(Order_content, on_delete=models.CASCADE)
    name            = models.CharField(max_length=50)
    quantityStatus  = models.IntegerField()
    unit            = models.CharField(max_length=20)
    note            = models.CharField(max_length=50)
    SKU             = models.CharField(max_length=30)
    status          = models.CharField(max_length=30)

class Content_history(models.Model):
    contentID   = models.ForeignKey(Order_content, on_delete=models.CASCADE)
    update_time = models.CharField(max_length=30)
    quantity    = models.IntegerField()
    unit        = models.CharField(max_length=20)

class Modifer_history(models.Model):
    mod_id      = models.ForeignKey(Order_modifer, on_delete=models.CASCADE)
    update_time = models.CharField(max_length=30)
    quantity    = models.IntegerField()
    unit        = models.CharField(max_length=20)

class KOMS_config(models.Model):
    print_or_display        = models.IntegerField()
    default_prepration_time = models.CharField(max_length=20)
    licence_key             = models.CharField(max_length=200)
    activation_status       = models.IntegerField()
    central_url             = models.CharField(max_length=30)
    send_order_to_cs        = models.BooleanField()

class Menu_sync(models.Model):
    isActive    = models.BooleanField(default=False)
    sync_mode   = models.IntegerField()
    sync_time   = models.CharField(max_length=40)
    sync_url    = models.CharField(max_length=100)
    provider    = models.CharField(max_length=200)
    sync_cred   = models.CharField(max_length=100)

class Prepration_time(models.Model):
    externalID      = models.CharField(max_length=20)
    tag             = models.CharField(max_length=50)
    prepration_time = models.CharField(max_length=100)


class Staff(models.Model):
    first_name      = models.CharField(max_length=100)
    last_name       = models.CharField(max_length=100)
    staff_type      = models.CharField(max_length=30)
    active_status   = models.IntegerField()
    station_id      = models.ForeignKey(Stations,on_delete=models.CASCADE,null=True, blank=True)

class Content_assign(models.Model):
    staffId     = models.ForeignKey(Staff, on_delete=models.CASCADE)
    contentID   = models.ForeignKey(Order_content, on_delete=models.CASCADE)

class UserSettings(models.Model):
    notification = models.BooleanField(default=True)
    cooking      = models.CharField(max_length=100,default=0xFF2E2E48)
    incoming     = models.CharField(max_length=100,default=0xFF2E2E48)
    dragged      = models.CharField(max_length=100,default=0xFF2E2E48)
    complete     = models.CharField(max_length=100,default=0xFF2E2E48)
    cancel       = models.CharField(max_length=100,default=0xFF2E2E48)
    recall       = models.CharField(max_length=100,default=0xFF2E2E48)
    priority     = models.CharField(max_length=100,default=0xFF2E2E48)
    nearTo       = models.CharField(max_length=100,default=0xFF2E2E48)
    stationId    = models.ForeignKey(Stations, on_delete=models.CASCADE,default=1,unique=True)



class OrderStatusName(models.Model):
    orderName = models.CharField(max_length = 50)
