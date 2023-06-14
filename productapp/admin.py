from django.contrib import admin
from productapp.models import Product
# Register your models here.
#admin.site.register(Product)

class ProductAdminClass(admin.ModelAdmin):
    list_display=['name','cat','price','status']
    list_filter=['status','cat']

admin.site.register(Product,ProductAdminClass)
admin.site.site_header="Royal Event Management"   