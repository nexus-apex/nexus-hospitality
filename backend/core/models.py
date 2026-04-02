from django.db import models

class HotelProperty(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, default="")
    property_type = models.CharField(max_length=50, choices=[("hotel", "Hotel"), ("resort", "Resort"), ("villa", "Villa"), ("hostel", "Hostel"), ("b&b", "B&B")], default="hotel")
    rooms = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("renovation", "Renovation"), ("closed", "Closed")], default="active")
    manager = models.CharField(max_length=255, blank=True, default="")
    contact = models.CharField(max_length=255, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class RoomBooking(models.Model):
    property_name = models.CharField(max_length=255)
    guest_name = models.CharField(max_length=255, blank=True, default="")
    room_type = models.CharField(max_length=50, choices=[("standard", "Standard"), ("deluxe", "Deluxe"), ("suite", "Suite"), ("villa", "Villa")], default="standard")
    check_in = models.DateField(null=True, blank=True)
    check_out = models.DateField(null=True, blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=[("confirmed", "Confirmed"), ("checked_in", "Checked In"), ("checked_out", "Checked Out"), ("cancelled", "Cancelled")], default="confirmed")
    source = models.CharField(max_length=50, choices=[("direct", "Direct"), ("ota", "OTA"), ("agent", "Agent")], default="direct")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.property_name

class HotelGuest(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, default="")
    phone = models.CharField(max_length=255, blank=True, default="")
    nationality = models.CharField(max_length=255, blank=True, default="")
    visits = models.IntegerField(default=0)
    total_spent = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    loyalty_tier = models.CharField(max_length=50, choices=[("member", "Member"), ("silver", "Silver"), ("gold", "Gold"), ("platinum", "Platinum")], default="member")
    preferences = models.TextField(blank=True, default="")
    vip = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
