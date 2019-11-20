from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Q
from django.contrib import auth
from django.core.mail import BadHeaderError, send_mail
from django.contrib import messages
from django.forms import ModelForm
from rideSharing.models import RideItem
from django.views.generic.edit import CreateView
from accountant.models import user_profile
from django.urls import reverse
from django import forms
from django.forms import TextInput
from django.core.paginator import Paginator

#This function gets all the items from the database
#and displays them to the screen sorted by most recently added
#param: request - array variable that is passed around the website, kinda like global variables
#returns: all the items in the database, with the most recently item added at the top
def index(request):

    #The CSS for this function can be found here
    template = 'rideSharing/index.html'
    #The title for the webpage
    title = "MTU Ridesharing"

    #Checks if the user is logged in
    if request.user.is_authenticated:

        #Gets 500 most recent items from the database and sorts by date added
        recent_items = RideItem.objects.filter(
            date_added__lte=timezone.now()
        ).order_by('-date_added')[:500]

        # Paginator will show 16 items per page
        paginator = Paginator(recent_items, 16, allow_empty_first_page=True)
        page = request.GET.get('page') # Gets the page number to display
        rides = paginator.get_page(page)
    

        #Packages the information to be displayed into context
        context = {
            'title': title,
            'rides': rides,
        }

        #Displays all the items from the database with repect to the CSS template
        return render(request, template, context)
    else:
        return HttpResponseRedirect('/')


class RideForm(ModelForm):
    class Meta:
        model = RideItem
        fields = ['start_city', 'start_state', 'start_zipcode', 'destination_city', 'destination_state', 'destination_zipcode', 'date_leaving', 'round_trip', 'return_date', 'spots', 'driver', 'notes', 'price']
        widgets = {'driver': TextInput(attrs={'readonly': 'readonly'})}

class RideCreate(CreateView):
    model = RideItem
    form_class = RideForm

    initial = {'start_city': "Houghton", 'start_state': "Michigan", 'start_zipcode': 49931}
    success_url = ''

    _this_user = None

    def setup(self, request, *args, **kwargs):
        self._this_user = user_profile.objects.get(user = request.user)
        self.initial['destination_city'] = self._this_user.home_city
        self.initial['destination_state'] = self._this_user.home_state
        self.initial['destination_zipcode'] = self._this_user.zipcode


        if self._this_user.preferred_name:
            # use user's preferred name if exists
            self.initial['driver'] = self._this_user.preferred_name
        else:
            self.initial['driver'] = request.user.get_short_name();

        super().setup(request, args, kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.username = self._this_user.user
        self.object.views = 0

        #self.object.username = self._this_user.user
        #self.object.views = 0

        self.object.save()

        return HttpResponseRedirect(reverse('rideSharing:index'))
