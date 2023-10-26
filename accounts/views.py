from django.shortcuts import render
from django.contrib import messages
from .forms import CustomerRegistrationForm, EmployeeRegistrationForm
from django.views import View
from .models import Customer, Employee, UserProfile
def register(request):
    return render(request, '../templates/register.html')

class CustomerRegisterationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'customer_register.html', {'form':form})
    def post(self, request): 
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            
            user = form.save()  # Save the user instance
            user_profile = UserProfile(user=user, is_customer=True)
            user_profile.save()

            # Create the Customer object with the associated user profile
            customer = Customer(user=user)
            customer.save()
            messages.success(request, 'Congratulations!! Registered Successfully')
            form.save()

        return render(request, 'customer_register.html', {'form':form})
    

class EmployeeRegisterationView(View):
    def get(self, request):
        form = EmployeeRegistrationForm()
        return render(request, 'employee_register.html', {'form':form})
    def post(self, request):
        form = EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user instance
            user_profile = UserProfile(user=user, is_employee=True)
            user_profile.save()

            # Create the Employee object with the associated user profile
            employee = Employee(user=user)
            employee.save()
            
            messages.success(request, 'Congratulations!! Registered Successfully')
            form.save()
        return render(request, 'employee_register.html', {'form':form})
