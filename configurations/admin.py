from django.contrib import admin
from .models import Location, Currency, ExchangeRate

# --- 1. Location Admin ---
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'created_at')
    search_fields = ('name', 'address')
    list_filter = ('created_at',)


# --- 2. Currency Admin ---
@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'symbol')
    search_fields = ('code', 'name')


# --- 3. ExchangeRate Admin ---
@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    # What fields to show in the list view
    list_display = ('__str__', 'base_currency', 'target_currency', 'rate', 'date')
    # Filter by date and currency
    list_filter = ('date', 'base_currency', 'target_currency')
    # Allow searching by rate or currency codes
    search_fields = ('rate', 'base_currency__code', 'target_currency__code')
    # Pre-populate Foreign Key fields with dropdowns
    raw_id_fields = ('base_currency', 'target_currency')