from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Snack(models.Model):
    """Model for all snack name. This model only contain name not stock"""

    id: models.BigAutoField = models.BigAutoField(primary_key=True)
    name: models.CharField = models.CharField(max_length=255, editable=True, unique=True)

    class Meta:
        # Order by name
        ordering = [
            "name",
        ]

    def __str__(self) -> str:
        return self.name


class Machine(models.Model):
    class MachineStatus(models.TextChoices):
        """
        NORMAL: all working find

        REFILL: some snacks are out

        OFFLINE: out of services
        """

        NORMAL = _("Normal")
        REFILL = _("Refill")
        OFFLINE = _("Offline")

    """Model for Vending machine contain machine individual information"""

    id: models.BigAutoField = models.BigAutoField(primary_key=True)
    name: models.CharField = models.CharField(max_length=255, unique=True, editable=True)
    location: models.TextField = models.TextField(
        max_length=500, editable=True, unique=True
    )
    # When create this machine shouldn't have any stock
    status: models.CharField = models.CharField(
        max_length=20,
        choices=MachineStatus.choices,
        default=MachineStatus.OFFLINE,
        editable=True,
    )

    class Meta:
        # Order by id
        ordering = [
            "id",
        ]

    def __str__(self) -> str:
        return f"Machine at {self.location}"


class Stock(models.Model):
    """Model for stock of vending machine"""

    id: models.BigAutoField = models.BigAutoField(primary_key=True)
    machine: models.ForeignKey = models.ForeignKey(to=Machine, on_delete=models.CASCADE)
    snack: models.ForeignKey = models.ForeignKey(to=Snack, on_delete=models.CASCADE)
    quantity: models.PositiveIntegerField = models.PositiveIntegerField(
        default=0, editable=True
    )

    class Meta:
        # Order by name
        ordering = [
            "id",
        ]
        default_related_name = "stock"
