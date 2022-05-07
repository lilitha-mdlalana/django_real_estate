from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import state_choices, price_choices,bedroom_choices


def index(request):
    listings = Listing.objects.all().order_by('-list_date').filter(is_published=True)[:3]
    context = {
        "listings" : listings,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,
    }
    return render(request,'pages/index.html',context)

def about(request):
    #Get all realtors
    realtors = Realtor.objects.order_by('-hire_data')
    #get mvp
    mvp_realtor = Realtor.objects.all().filter(is_mvp=True)
    context = {
        "mvp": mvp_realtor,
        "realtors":realtors
    }
    return render(request,'pages/about.html',context)

