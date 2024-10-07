from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Category, Customer, Product, Order, UserProfile


# Inline for UserProfile
class UserProfileInline(admin.StackedInline):  # Or admin.TabularInline
    model = UserProfile
    can_delete = False  # Disable deleting profiles directly in this view
    verbose_name_plural = 'Profile'  # Set the verbose name for the inline
    fields = ('phone', 'address')  # Fields to display in the inline
    extra = 0  # No extra empty forms


# Custom UserAdmin
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)  # Include the UserProfileInline

    # You can customize the displayed fields if necessary
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active')  # Display these fields
    search_fields = ('username', 'email')  # Enable search by username and email


# Admin view for Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Admin view for Customer
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('first_name', 'last_name')

# Admin view for Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_sale', 'sale_price', 'Category')
    search_fields = ('name',)
    list_filter = ('is_sale', 'Category')

# Admin view for Order
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'customer', 'quantity', 'date', 'status')
    search_fields = ('product__name', 'customer__first_name', 'customer__last_name')
    list_filter = ('status', 'date')

# Unregister the default UserAdmin to replace it with the custom one
admin.site.unregister(User)
admin.site.register(User, UserAdmin)  # Register the custom UserAdmin
admin.site.register(UserProfile)  # Optionally, you can register it separately as well
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
