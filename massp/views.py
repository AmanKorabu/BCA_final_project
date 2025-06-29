import json
from urllib import response
from django.shortcuts import render
from massp.models import Contact
from datetime import datetime
from massp.models import Appointment
from massp.models import Invoice
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas


# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth

from django.contrib.auth import authenticate, login
from django.db import IntegrityError
from django.contrib.auth import logout
from django.contrib import messages
from massp.forms import ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from massp.forms import AdminLoginForm

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                # Assuming 'admin_panel' is the correct URL pattern for the admin panel
                return redirect('/appointments/')  
            else:
                # Non-superusers should not access the admin panel, so redirect to a different page
                return redirect('more.html')  # Redirect to the home page or another appropriate page
        else:
            # Authentication failed, display an error message
            messages.error(request, 'Invalid username or password.')
    
    # For GET requests and failed authentication, or to display the login form initially
    return render(request, 'admin_login.html')


    # views.py
def more(request):
    return render(request, 'more.html')  

from massp.models import Product

def product_admin(request):
    products = Product.objects.all()
    return render(request, 'product_admin.html', {'products': products})

@login_required
def admin_panel(request):
    
    return render(request, 'admin_panel.html')    


def admin_logout(request):
    logout(request)
    return redirect('admin_login.html')  # Redirect to admin login page after logout


def view_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments.html', {'appointments': appointments})




# login logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

def SignupPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        
        if password != confirmPassword:
            # Passwords don't match, display an error message
            messages.error(request, 'Passwords do not match')
            return render(request, 'signup.html')
        
        try:
            # Attempt to create a new user
            data = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            data.save()
            # Redirect to the login page after successful signup
            return redirect('login.html')
        except IntegrityError:
            # If the username already exists, display an error message
            messages.error(request, 'Username already exists. Please choose a different username.')
            return render(request, 'signup.html')
    
    # If it's a GET request, render the signup page
    return render(request, 'signup.html')
def Loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('index.html')
        else:
            # If authentication fails, provide a notification
            message = 'Invalid username or password. Please try again.'
            messages.error(request, message)  # Adding error message
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
   

def logout_view(request):
    logout(request)
    return redirect('index')  # Redirect to the homepage or login page after logout
        
   

def index(request):
    return render(request, 'index.html')  


def profile(request):
    profile = request.user.profile
    return render(request, 'profile.html', {'profile': profile})
def profile_update(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
        else:
            messages.error(request, 'Error updating profile. Please correct the errors below.')
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'profile_update.html', {'form': form})
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def industrial(request):
    return render(request, 'industrial.html')

def powdercoating(request):
    return render(request, 'powdercoating.html')

def shotblasting(request):
    return render(request, 'shotblasting.html')
# views.py

from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def product_gallery(request):
    products = Product.objects.all()
    return render(request, 'product_gallery.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_admin')  # Redirect to the admin dashboard after adding the product
    else:
        form = ProductForm()
    return render(request, 'product_admin.html', {'form': form})

def delete_product(request, product_id):
    if request.method == 'DELETE':
        product = Product.objects.get(id=product_id)
        product.delete()
    return redirect('product_admin')  # Redirect to the admin dashboard after deleting the product

def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('product_gallery')  # Redirect to product gallery after deleting product


def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('product_gallery')


def contact(request):
    
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        Message = request.POST.get('Message')
       
        if len(name)<2 or len(email)<3 or len(phone)<10 : 
            messages.error(request,"please fill the form correctly")
        else:
            contact = Contact(name=name,email=email,Phone=phone,subject=subject,Message=Message,)
        contact.save()
        messages.success(request,'Your details submitted succesfully!!!Thank you')
    return render(request,'contact.html')
def apo(request):
    if request.method == 'POST':
        # Process form data and save appointment to database
            name=request.POST.get('name')
            email=request.POST.get('email')
            contact=request.POST.get('contact')
            date=request.POST.get('date')
            time=request.POST.get('time')
            purpose=request.POST.get('purpose')
            note=request.POST.get('note', '')
            status="pending"
            appointment =Appointment(name=name,email=email,contact=contact,date=date,time=time, purpose=purpose,note=note,status=status)
            appointment.save()
   
        
            messages.success(request,'Your details submitted succesfully!!!Thank you')
            
    return render(request, 'apo.html', {})
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

from massp.models import Appointment

def generate_monthly_report_appointment(request):
    # Get the year and month from the request
    year = request.GET.get('year')
    month = request.GET.get('month')

    # Fetch appointments for the specified month and year
    appointments = Appointment.objects.filter(date__year=year, date__month=month)

    # Generate PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="monthly_appointment_report_{year}_{month}.pdf"'

    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    # Add header
    styles = getSampleStyleSheet()
    header_style = styles['Title']
    header_text = f"Monthly Appointment Report - {month}/{year}"
    elements.append(Paragraph(header_text, header_style))
    elements.append(Spacer(1, 20))  # Add space between header and table

    # Add table for appointment data
    data = [['Name', 'Email', 'Contact', 'Date', 'Time', 'Purpose']]
    for appointment in appointments:
        data.append([
            appointment.name,
            appointment.email,
            appointment.contact,
            appointment.date.strftime('%Y-%m-%d'),
            appointment.time.strftime('%H:%M'),
            appointment.purpose
        ])

    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    table = Table(data)
    table.setStyle(table_style)
    elements.append(table)
    elements.append(Spacer(1, 20))  # Add space between table and footer

    # Build PDF
    doc.build(elements)
    return response

def generate_monthly_appointment_report_page(request):
    return render(request, 'generate_monthly_appointment_report.html')

    
def visit(request):
    return render(request,'visitUs.html')



def get_appointments(request):
    appointments = Appointment.objects.all()  # Retrieve all appointments from the database
    approved_count = Appointment.objects.filter(status='approved').count()
    canceled_count = Appointment.objects.filter(status='canceled').count()
    pending_count = Appointment.objects.filter(status='pending').count()
    total_count = approved_count + canceled_count + pending_count
    count = ({'total_count': total_count, 'pending_count': pending_count, 'approved_count': approved_count, 'canceled_count': canceled_count})

    return render(request, 'admin_panel.html', {'appointments': appointments, 'count':count})
def update_status(request):
    print("appointment_id", request)
    try:
        appointment = Appointment.objects.get(id=request.appointment_id)
        appointment.status = request.new_status
        appointment.save()
        return True  # Return True if update is successful
    except Appointment.DoesNotExist:
     return False

def my_api_view(request):
    if request.method == 'POST':
        # Retrieve POST data from request body
        try:
           
            post_data = json.loads(request.body.decode('utf-8'))
            print("post_data", post_data)
            appointment = Appointment.objects.get(id=post_data.get("appointment_id"))
            appointment.status = post_data.get("new_status")
            res=  appointment.save()
            return HttpResponse({"message": "POST request received", res: res}, status=200)  # Return True if update is successful
        except Appointment.DoesNotExist:
            return  HttpResponse({"message": "POST request received"}, status=200)
    else:
        return HttpResponse({"message": "Only POST requests are allowed"}, status=405)
    
def get_contacts(request):
    contacts = Contact.objects.all()  # Retrieve all contacts from the database
    return render(request, 'contacts.html', {'contacts': contacts})
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from django.http import HttpResponse

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Contact

def delete_contact(request, contact_id):
    if request.method == 'DELETE':
        contact = get_object_or_404(Contact, pk=contact_id)
        contact.delete()
        return JsonResponse({'message': 'Contact deleted successfully'}, status=200)
    else:
        return JsonResponse({'error': 'DELETE method required'}, status=405)


def invoice(request):
    if request.method == 'POST':
        # Extract data from the form
        customer_name = request.POST.get('customer_name')
        customer_address = request.POST.get('customer_address')
        customer_contact = request.POST.get('customer_contact')
        invoice_no = request.POST.get('invoice_no')
        invoice_date = request.POST.get('invoice_date')
        selected_service = request.POST.get('service')
        charges = float(request.POST.get('charges'))
        cgst = float(request.POST.get('cgst'))
        sgst = float(request.POST.get('sgst'))
        grand_total = float(request.POST.get('grand_total'))

           # Create an instance of the Invoice model
        invoice = Invoice(
            customer_name=customer_name,
            customer_address=customer_address,
            customer_contact=customer_contact,
            invoice_no=invoice_no,
            invoice_date=invoice_date,
            selected_service=selected_service,
            charges=charges,
            cgst=cgst,
            sgst=sgst,
            grand_total=grand_total
        )
        
        # Save the instance to the database
        invoice.save()
        # Create PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="invoice_{invoice_no}.pdf"'

        # Create PDF document
        doc = SimpleDocTemplate(response, pagesize=letter)
        elements = []

        # Add logo and company details
        logo = "static/images/IMAGES/20240121_160914.png"
        elements.append(Image(logo, width=170, height=120, hAlign='CENTER'))
        elements.append(Spacer(1, 10))  # Adjusted spacer
        elements.append(Paragraph("MASS COATING COMPANY", getSampleStyleSheet()["Title"]))
        elements.append(Paragraph("GAT NO.258/1, NEAR HOTEL MARROIT COURTYARD, KHALUMBRE, CHAKAN, PUNE-410501", getSampleStyleSheet()["Normal"]))
        elements.append(Spacer(1, 5))  # Adjusted spacer

        # Add company address on the right side below the company name
        company_address = [
            [""],
            ["Email: masscoating@gmail.com"],
            ["Tel: 9049957255"]
        ]
        company_address_table = Table(company_address, colWidths=[400])
        company_address_table.setStyle(TableStyle([('ALIGN', (-1, -4), (-1, -1), 'RIGHT')]))
        elements.append(company_address_table)
        elements.append(Spacer(1, 20))

        # Add invoice details
        elements.append(Paragraph("INVOICE", getSampleStyleSheet()["Heading2"]))
        elements.append(Paragraph(f"Invoice No: {invoice_no}", getSampleStyleSheet()["Normal"]))
        elements.append(Paragraph(f"Invoice Date: {invoice_date}", getSampleStyleSheet()["Normal"]))
        elements.append(Spacer(1, 20))

        # Add customer details
        elements.append(Paragraph("Customer Details:", getSampleStyleSheet()["Heading2"]))
        customer_info = [
            ["Name:", customer_name],
            ["Address:", customer_address],
            ["Contact:", customer_contact]
        ]
        customer_table = Table(customer_info, colWidths=[100, '*'])
        customer_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                                            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                                            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                            ('GRID', (0, 0), (-1, -1), 1, colors.black),
                                            ('BOX', (0, 0), (-1, -1), 1, colors.black)]))
        elements.append(customer_table)
        elements.append(Spacer(1, 20))

        # Add service details
        elements.append(Paragraph("Service Details:", getSampleStyleSheet()["Heading2"]))
        service_info = [
            ["Service:", selected_service],
            ["Charges:", f"Rs. {charges:.2f}"],  # Using the Indian Rupee symbol
            ["CGST (9%):", f"Rs. {cgst:.2f}"],
            ["SGST (9%):", f"Rs. {sgst:.2f}"],
            [Paragraph("Grand Total:", getSampleStyleSheet()["Normal"]), 
             Paragraph(f"Rs. {grand_total:.2f}", ParagraphStyle(name='Bold', fontName='Helvetica-Bold', textColor=colors.red))],  # Bold and red colored
        ]
        service_table = Table(service_info, colWidths=[100, '*'])
        service_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                                            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                                            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                            ('GRID', (0, 0), (-1, -1), 1, colors.black),
                                            ('BOX', (0, 0), (-1, -1), 1, colors.black)]))
        elements.append(service_table)

        # Add signature column
        signature_info = [
            ["Signature Of A/c:"],
            ["Name of A/c:"]
        ]
        signature_table = Table(signature_info, colWidths=[100])
        signature_table.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
                                             ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                                             ('LEFTPADDING', (0, 0), (-1, -1), 400)]))  # Adjust left padding to position at the right
        elements.append(Spacer(1, 10))  # Add some space between the service table and the signature column
        elements.append(signature_table)

        # Build PDF
        doc.build(elements)

        return response

    return render(request, 'invoice.html')
def get_invoices(request):
    # Fetch all invoices from the database
    invoices = Invoice.objects.all()

    # Pass the invoices to the template context
    return render(request, 'get_invoices.html', {'invoices': invoices})
# views.py
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from .models import Invoice

def generate_monthly_report(request):
    # Get the year and month from the request
    year = request.GET.get('year')
    month = request.GET.get('month')

    # Fetch invoices for the specified month and year
    invoices = Invoice.objects.filter(invoice_date__year=year, invoice_date__month=month)

    # Generate PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="monthly_report_{year}_{month}.pdf"'

    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    # Add header
    styles = getSampleStyleSheet()
    header_style = styles['Title']
    header_text = f"Monthly Report of invoices - {month}/{year}"
    elements.append(Paragraph(header_text, header_style))
    elements.append(Spacer(1, 20))  # Add space between header and table

    # Add table for invoice data
    data = [['Invoice No.', 'Customer Name',  'Customer Contact', 'Invoice Date', 'Selected Service',  'Grand Total']]
    for invoice in invoices:
        data.append([
            invoice.invoice_no,
            invoice.customer_name,
            # invoice.customer_address,
            invoice.customer_contact,
            invoice.invoice_date.strftime('%Y-%m-%d'),
            invoice.selected_service,
            # f"Rs. {invoice.charges:.2f}",
            # f"Rs. {invoice.cgst:.2f}",
            # f"Rs. {invoice.sgst:.2f}",
            f"Rs. {invoice.grand_total:.2f}"
        ])

    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    table = Table(data)
    table.setStyle(table_style)
    elements.append(table)
    elements.append(Spacer(1, 20))  # Add space between table and footer

    # Build PDF
    doc.build(elements)
    return response
def generate_monthly_report_form(request):
    return render(request, 'generate_monthly_report_form.html')
