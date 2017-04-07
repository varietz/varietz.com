# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AwsBs(models.Model):
    dt = models.DateField()
    cat = models.CharField(max_length=10, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    asin = models.CharField(max_length=20)
    url = models.CharField(max_length=150, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aws_bs'
        unique_together = (('dt', 'asin'),)


class Daily(models.Model):
    comp = models.CharField(max_length=45)
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    product = models.CharField(db_column='Product', max_length=150, blank=True, null=True)  # Field name made lowercase.
    style = models.CharField(db_column='Style', max_length=45)  # Field name made lowercase.
    mrp = models.DecimalField(db_column='MRP', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    article_type = models.CharField(db_column='Article_Type', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rnk = models.IntegerField(db_column='Rnk', blank=True, null=True)  # Field name made lowercase.
    pic_url = models.CharField(max_length=500, blank=True, null=True)
    brand = models.CharField(db_column='Brand', max_length=100, blank=True, null=True)  # Field name made lowercase.
    offer = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daily'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FlBs(models.Model):
    dt = models.DateField()
    cat = models.CharField(max_length=10, blank=True, null=True)
    fid = models.CharField(db_column='FID', max_length=11)  # Field name made lowercase.
    rank = models.IntegerField(db_column='Rank', blank=True, null=True)  # Field name made lowercase.
    pname = models.CharField(db_column='pName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    keyspec = models.CharField(db_column='keySpec', max_length=100, blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(blank=True, null=True)
    finalprice = models.IntegerField(db_column='finalPrice', blank=True, null=True)  # Field name made lowercase.
    deliverycharge = models.IntegerField(db_column='deliveryCharge', blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(blank=True, null=True)
    ratingcnt = models.IntegerField(db_column='ratingCnt', blank=True, null=True)  # Field name made lowercase.
    reviews = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fl_bs'
        unique_together = (('dt', 'fid'),)


class FlProductCat(models.Model):
    cat = models.CharField(primary_key=True, max_length=10)
    category_name = models.CharField(max_length=45)
    type = models.CharField(db_column='Type', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fl_product_cat'


class Piclib(models.Model):
    comp = models.CharField(max_length=45)
    style = models.CharField(max_length=45)
    src = models.CharField(max_length=500, blank=True, null=True)
    des = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'piclib'
        unique_together = (('comp', 'style'),)


class ProductCat(models.Model):
    comp = models.CharField(max_length=20)
    cat = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'product_cat'
        unique_together = (('comp', 'cat'),)
