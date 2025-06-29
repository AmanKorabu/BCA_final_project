from django.contrib import admin
from django.urls import path, include
from massp import views
from massp.views import Loginpage, generate_monthly_report_form, get_appointments, get_invoices, my_api_view, update_status, get_contacts, admin_login, generate_monthly_report
from django.conf import settings
from django.conf.urls.static import static
from massp.views import generate_monthly_report_appointment,generate_monthly_appointment_report_page,product_gallery

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.more, name='more'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_logout.html/', views.admin_logout, name='admin_logout'),
    path('admin_panel.html/', views.admin_panel, name='admin_panel'),
    path('signup.html', views.SignupPage, name='signup'),
    path('login.html', views.Loginpage, name='login'),
     path("more.html",views.more,name='more'),
    path("index.html",views.index,name='HOME'),
    path('profile_update.html', views.profile_update, name='profile_update'),
    path("profile.html",views.profile,name='profile'),
    path("about.html",views.about,name='about'),
    path("services.html",views.services,name='services'),
      path("industrial.html",views.industrial,name='industrial'),
        path("powdercoating.html",views.powdercoating,name='powdercoating'),
          path("shotblasting.html",views.shotblasting,name='shotblasting'),
    path("product_gallery.html",views.product_gallery,name='product_gallery'),
    path('add_product/', views.add_product, name='add_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path("contact.html",views.contact,name='contact'),
    path("apo.html",views.apo,name='appointment'),
    path("visitUs.html",views.visit,name='visit us'), 
      path("contacts.html",views.contact,name='contact'),
           path("invoice.html",views.invoice,name='invoice'),
    path('appointments/', views.get_appointments, name='appointments'),
    path('update_status/', views.update_status, name='update_status'),
    path('my_api_view/', views.my_api_view, name='my_api_view'),
    path('contacts/', views.get_contacts, name='appointments'),
    path('get_invoices.html', get_invoices, name='get_invoices'),
    path('generate_monthly_report/', generate_monthly_report, name='generate_monthly_report'),
    path('generate_monthly_report_form/',generate_monthly_report_form, name='generate_monthly_report_form'),
      path('generate-monthly-report/',generate_monthly_report_appointment, name='generate_monthly_report_appointment'),
       path('generate_monthly_appointment_report/', views.generate_monthly_appointment_report_page, name='generate_monthly_appointment_report_page'),
     path('delete_contact/<int:contact_id>/', views.delete_contact, name='delete_contact'),
     path('product-admin/', views.product_admin, name='product_admin'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
