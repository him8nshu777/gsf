from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm

# from accounts.form import CustomPasswordResetForm
urlpatterns = [
    path('register/', views.register, name='register'),
    path('customer_register/', views.CustomerRegisterationView.as_view(),name='customer_register'),
    path('employee_register/', views.EmployeeRegisterationView.as_view(),name='employee_register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path("logout/", auth_views.LogoutView.as_view(next_page='login'), name="logout"),

    path("passwordchange/", auth_views.PasswordChangeView.as_view(template_name = 'passwordchange.html', form_class = MyPasswordChangeForm, success_url='/passwordchangedone/'), name="passwordchange"),

    path("passwordchangedone/", auth_views.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'), name="passwordchangedone"),

    # password reset
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='password_reset.html', 
    form_class=MyPasswordResetForm), name='password_reset'),
    
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),

    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),

    path("password-reset-complete", auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    # password reset 



]