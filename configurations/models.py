from django.db import models

# 1. Location Model (Singular, PascalCase)
class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Locations'
        ordering = ['name']
        # db_table is omitted, Django uses appname_location

    def __str__(self):
        return self.name


# 2. Currency Model (Singular, PascalCase)
class Currency(models.Model):
    code = models.CharField(max_length=10, unique=True)  # e.g., 'USD'
    name = models.CharField(max_length=50)              # e.g., 'United States Dollar'
    symbol = models.CharField(max_length=5, blank=True, null=True) # e.g., '$'

    class Meta:
        verbose_name_plural = 'Currencies'
        ordering = ['code']
        # db_table is omitted, Django uses appname_currency

    def __str__(self):
        return f"[{self.code}] {self.name}"


# 3. ExchangeRate Model (Singular, PascalCase)
class ExchangeRate(models.Model):
    # base_currency: The currency the rate is FROM (1 unit of this currency)
    base_currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        related_name='rates_as_base',
        help_text='The currency this rate is against (the base).'
    )

    # target_currency: The currency the rate is TO (X units of this currency)
    target_currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        related_name='rates_as_target',
        help_text='The currency whose value is being quoted (the target).'
    )

    # Rate: 1 unit of base_currency = X units of target_currency
    rate = models.DecimalField(max_digits=10, decimal_places=4)
    date = models.DateField()

    class Meta:
        verbose_name_plural = 'Exchange Rates'
        ordering = ['-date', 'base_currency__code', 'target_currency__code']
        # Ensures only one rate exists for a specific currency pair on a given day
        unique_together = ('base_currency', 'target_currency', 'date')
        # db_table is omitted, Django uses appname_exchangerate

    def __str__(self):
        return f"1 {self.base_currency.code} = {self.rate} {self.target_currency.code} on {self.date}"