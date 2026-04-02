import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import HotelProperty, RoomBooking, HotelGuest


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['hotelproperty_count'] = HotelProperty.objects.count()
    ctx['hotelproperty_hotel'] = HotelProperty.objects.filter(property_type='hotel').count()
    ctx['hotelproperty_resort'] = HotelProperty.objects.filter(property_type='resort').count()
    ctx['hotelproperty_villa'] = HotelProperty.objects.filter(property_type='villa').count()
    ctx['hotelproperty_total_rating'] = HotelProperty.objects.aggregate(t=Sum('rating'))['t'] or 0
    ctx['roombooking_count'] = RoomBooking.objects.count()
    ctx['roombooking_standard'] = RoomBooking.objects.filter(room_type='standard').count()
    ctx['roombooking_deluxe'] = RoomBooking.objects.filter(room_type='deluxe').count()
    ctx['roombooking_suite'] = RoomBooking.objects.filter(room_type='suite').count()
    ctx['roombooking_total_amount'] = RoomBooking.objects.aggregate(t=Sum('amount'))['t'] or 0
    ctx['hotelguest_count'] = HotelGuest.objects.count()
    ctx['hotelguest_member'] = HotelGuest.objects.filter(loyalty_tier='member').count()
    ctx['hotelguest_silver'] = HotelGuest.objects.filter(loyalty_tier='silver').count()
    ctx['hotelguest_gold'] = HotelGuest.objects.filter(loyalty_tier='gold').count()
    ctx['hotelguest_total_total_spent'] = HotelGuest.objects.aggregate(t=Sum('total_spent'))['t'] or 0
    ctx['recent'] = HotelProperty.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def hotelproperty_list(request):
    qs = HotelProperty.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(property_type=status_filter)
    return render(request, 'hotelproperty_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def hotelproperty_create(request):
    if request.method == 'POST':
        obj = HotelProperty()
        obj.name = request.POST.get('name', '')
        obj.location = request.POST.get('location', '')
        obj.property_type = request.POST.get('property_type', '')
        obj.rooms = request.POST.get('rooms') or 0
        obj.rating = request.POST.get('rating') or 0
        obj.status = request.POST.get('status', '')
        obj.manager = request.POST.get('manager', '')
        obj.contact = request.POST.get('contact', '')
        obj.save()
        return redirect('/hotelproperties/')
    return render(request, 'hotelproperty_form.html', {'editing': False})


@login_required
def hotelproperty_edit(request, pk):
    obj = get_object_or_404(HotelProperty, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.location = request.POST.get('location', '')
        obj.property_type = request.POST.get('property_type', '')
        obj.rooms = request.POST.get('rooms') or 0
        obj.rating = request.POST.get('rating') or 0
        obj.status = request.POST.get('status', '')
        obj.manager = request.POST.get('manager', '')
        obj.contact = request.POST.get('contact', '')
        obj.save()
        return redirect('/hotelproperties/')
    return render(request, 'hotelproperty_form.html', {'record': obj, 'editing': True})


@login_required
def hotelproperty_delete(request, pk):
    obj = get_object_or_404(HotelProperty, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/hotelproperties/')


@login_required
def roombooking_list(request):
    qs = RoomBooking.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(property_name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(room_type=status_filter)
    return render(request, 'roombooking_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def roombooking_create(request):
    if request.method == 'POST':
        obj = RoomBooking()
        obj.property_name = request.POST.get('property_name', '')
        obj.guest_name = request.POST.get('guest_name', '')
        obj.room_type = request.POST.get('room_type', '')
        obj.check_in = request.POST.get('check_in') or None
        obj.check_out = request.POST.get('check_out') or None
        obj.amount = request.POST.get('amount') or 0
        obj.status = request.POST.get('status', '')
        obj.source = request.POST.get('source', '')
        obj.save()
        return redirect('/roombookings/')
    return render(request, 'roombooking_form.html', {'editing': False})


@login_required
def roombooking_edit(request, pk):
    obj = get_object_or_404(RoomBooking, pk=pk)
    if request.method == 'POST':
        obj.property_name = request.POST.get('property_name', '')
        obj.guest_name = request.POST.get('guest_name', '')
        obj.room_type = request.POST.get('room_type', '')
        obj.check_in = request.POST.get('check_in') or None
        obj.check_out = request.POST.get('check_out') or None
        obj.amount = request.POST.get('amount') or 0
        obj.status = request.POST.get('status', '')
        obj.source = request.POST.get('source', '')
        obj.save()
        return redirect('/roombookings/')
    return render(request, 'roombooking_form.html', {'record': obj, 'editing': True})


@login_required
def roombooking_delete(request, pk):
    obj = get_object_or_404(RoomBooking, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/roombookings/')


@login_required
def hotelguest_list(request):
    qs = HotelGuest.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(loyalty_tier=status_filter)
    return render(request, 'hotelguest_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def hotelguest_create(request):
    if request.method == 'POST':
        obj = HotelGuest()
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.nationality = request.POST.get('nationality', '')
        obj.visits = request.POST.get('visits') or 0
        obj.total_spent = request.POST.get('total_spent') or 0
        obj.loyalty_tier = request.POST.get('loyalty_tier', '')
        obj.preferences = request.POST.get('preferences', '')
        obj.vip = request.POST.get('vip') == 'on'
        obj.save()
        return redirect('/hotelguests/')
    return render(request, 'hotelguest_form.html', {'editing': False})


@login_required
def hotelguest_edit(request, pk):
    obj = get_object_or_404(HotelGuest, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.nationality = request.POST.get('nationality', '')
        obj.visits = request.POST.get('visits') or 0
        obj.total_spent = request.POST.get('total_spent') or 0
        obj.loyalty_tier = request.POST.get('loyalty_tier', '')
        obj.preferences = request.POST.get('preferences', '')
        obj.vip = request.POST.get('vip') == 'on'
        obj.save()
        return redirect('/hotelguests/')
    return render(request, 'hotelguest_form.html', {'record': obj, 'editing': True})


@login_required
def hotelguest_delete(request, pk):
    obj = get_object_or_404(HotelGuest, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/hotelguests/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['hotelproperty_count'] = HotelProperty.objects.count()
    data['roombooking_count'] = RoomBooking.objects.count()
    data['hotelguest_count'] = HotelGuest.objects.count()
    return JsonResponse(data)
