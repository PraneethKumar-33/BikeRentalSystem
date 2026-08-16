from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Bike, Customer, Booking, Review
from .forms import UserRegistrationForm, BookingForm, ReviewForm, BikeForm
def is_admin(user):
    return user.is_superuser
# 1. Home Page / Dashboard
def index(request):
    if request.user.is_authenticated:
        # Fetch ALL bikes
        bikes = Bike.objects.all()
        return render(request, 'rentals/index.html', {'bikes': bikes})
    else:
        # Show Landing Page
        return render(request, 'rentals/index.html')

# 2. Registration Logic
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            
            Customer.objects.create(
                user=user,
                phone_number=form.cleaned_data['phone_number']
            )
            
            login(request, user)
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 'rentals/register.html', {'form': form})

# 3. New: Bike Details Page (Shows Reviews & Book Button)
@login_required(login_url='/login/')
def bike_details(request, bike_id):
    bike = get_object_or_404(Bike, pk=bike_id)
    reviews = bike.reviews.all().order_by('-created_at')
    
    # Calculate average rating
    avg_rating = 0
    if reviews:
        avg_rating = sum(r.rating for r in reviews) / len(reviews)

    return render(request, 'rentals/bike_details.html', {
        'bike': bike, 
        'reviews': reviews, 
        'avg_rating': round(avg_rating, 1),
    })

# 4. Booking Logic
@login_required(login_url='/login/')
def book_bike(request, bike_id):
    bike = get_object_or_404(Bike, pk=bike_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user.customer
            booking.bike = bike
            booking.save()
            return redirect('index')
    else:
        form = BookingForm()
    
    return render(request, 'rentals/book_bike.html', {'form': form, 'bike': bike})

# 5. My Rentals Page
@login_required(login_url='/login/')
def my_rentals(request):
    bookings = Booking.objects.filter(customer=request.user.customer).select_related('bike')
    return render(request, 'rentals/my_rentals.html', {'bookings': bookings})

@login_required(login_url='/login/')
def return_bike(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, customer=request.user.customer)
    
    # --- NEW: Calculate the Cost ---
    # Calculate the number of days
    delta = booking.end_date - booking.start_date
    days = delta.days
    
    # If returned same day, count as 1 day
    if days == 0:
        days = 1
        
    # Calculate Total
    total_cost = days * booking.bike.daily_rate
    # -------------------------------

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Save Review
            review = form.save(commit=False)
            review.bike = booking.bike
            review.user = request.user
            review.save()
            
            # Return Bike
            bike = booking.bike
            bike.availability = True
            bike.save()
            
            # Delete Booking
            booking.delete()
            
            return redirect('my_rentals')
    else:
        form = ReviewForm()
    
    # Pass 'total_cost' and 'days' to the template
    return render(request, 'rentals/return_bike.html', {
        'form': form, 
        'booking': booking,
        'days': days,
        'total_cost': total_cost
    })
#1. Admin Dashboard (List all bikes with Edit/Delete buttons)
@user_passes_test(is_admin, login_url='/login/')
def admin_dashboard(request):
    bikes = Bike.objects.all().order_by('-id') # Newest first
    return render(request, 'rentals/admin_dashboard.html', {'bikes': bikes})

# 2. Add New Bike
@user_passes_test(is_admin, login_url='/login/')
def add_bike(request):
    if request.method == 'POST':
        form = BikeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = BikeForm()
    return render(request, 'rentals/bike_form.html', {'form': form, 'title': 'Add New Bike'})

# 3. Edit Bike
@user_passes_test(is_admin, login_url='/login/')
def edit_bike(request, bike_id):
    bike = get_object_or_404(Bike, pk=bike_id)
    if request.method == 'POST':
        form = BikeForm(request.POST, instance=bike)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = BikeForm(instance=bike)
    return render(request, 'rentals/bike_form.html', {'form': form, 'title': 'Edit Bike'})

# 4. Delete Bike
@user_passes_test(is_admin, login_url='/login/')
def delete_bike(request, bike_id):
    bike = get_object_or_404(Bike, pk=bike_id)
    if request.method == 'POST':
        bike.delete()
        return redirect('admin_dashboard')
    return render(request, 'rentals/bike_confirm_delete.html', {'bike': bike})