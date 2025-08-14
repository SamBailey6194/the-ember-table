from django.db import models
from django.utils import timezone


# Create your models here.
class Menu(models.Model):
    """
    Allows admin control over whether a menu is standard or seasonal
    Seasonal menus have start/end dates and activation status
    """
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    auto_renew_yearly = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def is_currently_active(self):
        """
        Helps determine if the menu is active
        """
        today = timezone.now().date()
        if self.start_date and self.end_date:
            return self.is_active and self.start_date <= today <= self.end_date
        return self.is_active

    def renew_for_next_year(self):
        """
        Creates menu for next year with shifted dates when admin selects to
        """
        should_renew = (
            self.auto_renew_yearly and
            self.end_date and
            timezone.now().date() > self.end_date
        )
        if should_renew:
            new_start = (
                self.start_date.replace(year=self.start_date.year + 1)
                if self.start_date else None
                )
            new_end = (
                self.end_date.replace(year=self.end_date.year + 1)
                if self.end_date else None
                )
            return Menu.objects.create(
                name=self.name + " (Next Year)",
                is_active=True,
                start_date=new_start,
                end_date=new_end,
                auto_renew_yearly=self.auto_renew_yearly
            )
        return None

    def auto_renew_if_needed(self):
        return self.renew_for_next_year()


class MenuItem(models.Model):
    """
    Allows admin to create menu items and they get added to the correct menu
    """
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name='items'
        )
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.menu.name})"
