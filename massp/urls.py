from django.contrib import admin
from django.urls import path
from massp import views
from massp.views import profile_update






urlpatterns = [
    
    path("more.html",views.more,name='more'),
    path("index.html",views.index,name='HOME'),
    path('profile_update.html', views.profile_update, name='profile_update'),
    path("profile.html",views.profile,name='profile'),
    path('admin_login/', views.admin_login, name='admin_login'),
     path('admin_panel.html/', views.admin_panel, name='admin_panel'),
     
    path("about.html",views.about,name='about'),
    path("services.html",views.services,name='services'),
      path("industrial.html",views.industrial,name='industrial'),
        path("powdercoating.html",views.powdercoating,name='powdercoating'),
          path("shotblasting.html",views.shotblasting,name='shotblasting'),
    path("product_gallery.html/",views.product_gallery,name='product_gallery'),
    path('add_product/', views.add_product, name='add_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path("contact.html",views.contact,name='contact'),
    path("apo.html",views.apo,name='appointment'),
    path("visitUs.html",views.visit,name='visit us'), 
      path("contacts.html",views.contact,name='contact'),
           path("invoice.html",views.invoice,name='invoice'),
           path('get_invoices.html', views.get_invoices, name='get_invoices'),
            path('generate_monthly_report_form/', views.generate_monthly_report_form, name='generate_monthly_report_form'),
           path('generate_monthly_report/', views.generate_monthly_report, name='generate_monthly_report'),
            path('generate-monthly-report/', views.generate_monthly_report_appointment, name='generate_monthly_report_appointment'),
            path('generate_monthly_appointment_report/', views.generate_monthly_appointment_report_page, name='generate_monthly_appointment_report_page'),
           path('delete_contact/<int:contact_id>/', views.delete_contact, name='delete_contact'),
           path('product-admin/', views.product_admin, name='product_admin'),
           
]
