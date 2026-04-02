from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import HotelProperty, RoomBooking, HotelGuest
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusHospitality with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexushospitality.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if HotelProperty.objects.count() == 0:
            for i in range(10):
                HotelProperty.objects.create(
                    name=f"Sample HotelProperty {i+1}",
                    location=f"Sample {i+1}",
                    property_type=random.choice(["hotel", "resort", "villa", "hostel", "b&b"]),
                    rooms=random.randint(1, 100),
                    rating=round(random.uniform(1000, 50000), 2),
                    status=random.choice(["active", "renovation", "closed"]),
                    manager=f"Sample {i+1}",
                    contact=f"Sample {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 HotelProperty records created'))

        if RoomBooking.objects.count() == 0:
            for i in range(10):
                RoomBooking.objects.create(
                    property_name=f"Sample RoomBooking {i+1}",
                    guest_name=f"Sample RoomBooking {i+1}",
                    room_type=random.choice(["standard", "deluxe", "suite", "villa"]),
                    check_in=date.today() - timedelta(days=random.randint(0, 90)),
                    check_out=date.today() - timedelta(days=random.randint(0, 90)),
                    amount=round(random.uniform(1000, 50000), 2),
                    status=random.choice(["confirmed", "checked_in", "checked_out", "cancelled"]),
                    source=random.choice(["direct", "ota", "agent"]),
                )
            self.stdout.write(self.style.SUCCESS('10 RoomBooking records created'))

        if HotelGuest.objects.count() == 0:
            for i in range(10):
                HotelGuest.objects.create(
                    name=["Rajesh Kumar","Priya Sharma","Amit Patel","Deepa Nair","Vikram Singh","Ananya Reddy","Suresh Iyer","Meera Joshi","Karthik Rao","Fatima Khan"][i],
                    email=f"demo{i+1}@example.com",
                    phone=f"+91-98765{43210+i}",
                    nationality=f"Sample {i+1}",
                    visits=random.randint(1, 100),
                    total_spent=round(random.uniform(1000, 50000), 2),
                    loyalty_tier=random.choice(["member", "silver", "gold", "platinum"]),
                    preferences=f"Sample preferences for record {i+1}",
                    vip=random.choice([True, False]),
                )
            self.stdout.write(self.style.SUCCESS('10 HotelGuest records created'))
