from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        "room",
        "status",
        "guest",
        "check_in",
        "check_out",
        "in_progress",
    )

    list_filter = ("status",)