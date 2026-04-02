from django.contrib import admin
from .models import HotelProperty, RoomBooking, HotelGuest

@admin.register(HotelProperty)
class HotelPropertyAdmin(admin.ModelAdmin):
    list_display = ["name", "location", "property_type", "rooms", "rating", "created_at"]
    list_filter = ["property_type", "status"]
    search_fields = ["name", "location", "manager"]

@admin.register(RoomBooking)
class RoomBookingAdmin(admin.ModelAdmin):
    list_display = ["property_name", "guest_name", "room_type", "check_in", "check_out", "created_at"]
    list_filter = ["room_type", "status", "source"]
    search_fields = ["property_name", "guest_name"]

@admin.register(HotelGuest)
class HotelGuestAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "nationality", "visits", "created_at"]
    list_filter = ["loyalty_tier"]
    search_fields = ["name", "email", "phone"]
