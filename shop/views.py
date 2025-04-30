from django.shortcuts import render
from .models import Visitor, Order
from django.db.models import Q, Count, Sum
from django.db.models.functions import TruncDate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from authentication.views import *
# Create your views here.


def index(request):
    visitor, created = Visitor.objects.get_or_create(pk=1)
    visitor.count += 1
    visitor.save()
    return render(request, 'index.html')

@login_required
def admin_dashboard(request):
    
    return render(request, 'authentication/dashboard.html')


def contact(request):
    
    return render(request, 'contact.html')

def products(request):
    
    return render(request, 'products.html')

def about(request):
    
    return render(request, 'about.html')

@login_required
def order_stats(request):
  # Pie Chart Data: Payment Status Breakdown
    status_counts = (
        Order.objects.values('payment_status')
        .annotate(count=Count('payment_status'))
    )
    pie_labels = [entry['payment_status'].capitalize() for entry in status_counts]
    pie_data = [entry['count'] for entry in status_counts]

    # Bar Chart Data: Units Sold Per Day
    daily_sales = (
        Order.objects.annotate(date_only=TruncDate('date'))
        .values('date_only')
        .annotate(total_quantity=Sum('quantity'))
        .order_by('date_only')
    )
    bar_labels = [
    entry['date_only'].strftime('%Y-%m-%d') if entry['date_only'] else 'Unknown'
    for entry in daily_sales
]
    bar_data = [entry['total_quantity'] for entry in daily_sales]

    context = {
        'pie_labels': pie_labels,
        'pie_data': pie_data,
        'bar_labels': bar_labels,
        'bar_data': bar_data,
    }
    return render(request, 'sales_report/sales_report.html', context)




@login_required
def client_orders(request):
    query = request.GET.get('q', '')
    if query:
        orders = Order.objects.filter(
            Q(full_name__icontains=query) | Q(phone_number__icontains=query)
        ).order_by('-date')
    else:
        orders = Order.objects.all().order_by('-date')

    return render(request, 'sales_report/clients_list.html', {'orders': orders, 'query': query})

def success(request):
    
    return render(request, 'success.html')

@login_required
def sales_entry(request):
    if request.method == 'POST':
        Order.objects.create(
            full_name=request.POST['full_name'],
            phone_number=request.POST['phone_number'],
            quantity=request.POST['quantity'],
            description=request.POST.get('description', ''),
            payment_status=request.POST.get('payment_status', 'pending'),
            comments=request.POST.get('comments', '')
        )
        return render(request, 'success.html')  # Replace with your success page
    
    return render(request, 'sales_report/sales_entry.html')