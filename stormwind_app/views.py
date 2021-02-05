from django.shortcuts import render
from .models import *
from django.views.generic import *
from .forms import *
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.views import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

class SuccessMessage:
    @property
    def success_msg(self):
        return False
    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

class HomeListView(ListView):
    model = Offer
    template_name = 'home.html'
    context_object_name = 'home'

#************************
#Property classes
class PropertyListView(ListView):
    model = Property
    template_name = 'property.html'
    context_object_name = 'property'
    def get_context_data(self, **kwargs):
        kwargs['list_propery'] = Offer.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)

class PropertyDetailView(DetailView):
    model = Property
    template_name = 'detail_property.html'
    context_object_name = 'get_property'

class PropertyCreateView(LoginRequiredMixin, SuccessMessage, CreateView):
    model = Property
    template_name = 'add_property.html'
    form_class = PropertyForm
    success_url = reverse_lazy('add_property')
    success_msg = 'Собственность добавлена'
    def get_context_data(self, **kwargs):
        kwargs['list_property'] = Property.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)
    def form_valid(self, form, **kwargs):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

class PropertyUpdateView(LoginRequiredMixin, UpdateView):
    model = Property
    template_name = 'add_property.html'
    form_class = PropertyForm
    success_url = reverse_lazy('add_property')
    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs

class PropertyDeleteView(LoginRequiredMixin, DeleteView):
    model = Property
    template_name = 'add_property.html'
    success_url = reverse_lazy('add_property')
    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user !=  self.object.author:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)

#**********************
## Client classess

class СlientListView(ListView):
    model = Client
    template_name = 'clients.html'
    context_object_name = 'clients'
    def get_context_data(self, **kwargs):
        kwargs['list_clients'] = Offer.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)

class ClientsDetailView(DetailView):
    model = Client
    template_name = 'detail_client.html'
    context_object_name = 'get_client'

class ClientCreateView(LoginRequiredMixin, SuccessMessage, CreateView):
    model = Client
    template_name = 'add_client.html'
    form_class = ClientForm
    success_url = reverse_lazy('add_client')
    success_msg = 'Клиент_добавлен'
    def get_context_data(self, **kwargs):
        kwargs['list_clients'] = Client.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)
    def form_valid(self, form, **kwargs):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    template_name = 'add_client.html'
    form_class = ClientForm
    success_url = reverse_lazy('clients')
    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs

class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'add_client.html'
    success_url = reverse_lazy('add_client')
    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user !=  self.object.author:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)

#***********************
#Realtor classess

class RealtorListView(ListView):
    model = Realtor
    template_name = 'realtors.html'
    context_object_name = 'realtors'
    def get_context_data(self, **kwargs):
        kwargs['list_realtors'] = Realtor.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)

class RealtorDetailView(DetailView):
    model = Realtor
    template_name = 'detail_realtor.html'
    context_object_name = 'get_realtor'

class RealtorCreateView(LoginRequiredMixin, SuccessMessage, CreateView):
    model = Realtor
    template_name = 'add_realtor.html'
    form_class = RealtorForm
    success_url = reverse_lazy('add_realtor')
    success_msg = 'Риэлтор_добавлен'
    def get_context_data(self, **kwargs):
        kwargs['list_realtors'] = Realtor.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)
    def form_valid(self, form, **kwargs):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

class RealtorUpdateView(LoginRequiredMixin, UpdateView):
    model = Realtor
    template_name = 'add_realtor.html'
    form_class = RealtorForm
    success_url = reverse_lazy('realtors')
    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs

class RealtorDeleteView(LoginRequiredMixin, DeleteView):
    model = Realtor
    template_name = 'add_realtor.html'
    success_url = reverse_lazy('add_realtor')
    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user !=  self.object.author:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)

##**********************
##Offer classess

class OffersListView(ListView):
    model = Offer
    template_name = 'offers.html'
    context_object_name = 'offers'
    def get_context_data(self, **kwargs):
        kwargs['list_offers'] = Offer.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)

class OffersDetailView(DetailView):
    model = Offer
    template_name = 'detail.html'
    context_object_name = 'get_offer'

class OfferCreateView(LoginRequiredMixin, SuccessMessage, CreateView):
    model = Offer
    template_name = 'add_offer.html'
    form_class = OfferForm
    success_url = reverse_lazy('add_offer')
    success_msg = 'Предложение добавлено'
    def get_context_data(self, **kwargs):
        kwargs['list_offers'] = Offer.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)
    def form_valid(self, form, **kwargs):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.price_percent = self.object.price + ((self.object.price/100) * 3)
        self.object.save()
        return super().form_valid(form)

class OfferUpdateView(LoginRequiredMixin, UpdateView):
    model = Offer
    template_name = 'add_offer.html'
    form_class = OfferForm
    success_url = reverse_lazy('offers')
    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs

class OfferDeleteView(LoginRequiredMixin, DeleteView):
    model = Offer
    template_name = 'add_req.html'
    success_url = reverse_lazy('add_offer')
    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user !=  self.object.author:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)

#********************
#Requirement classses

class ReqsListView(ListView):
    model = Req
    template_name = 'reqs.html'
    context_object_name = 'reqs'

class ReqsDetailView(LoginRequiredMixin, DetailView):
    model = Req
    template_name = 'detail_req.html'
    context_object_name = 'get_req'

class ReqsCreateView(LoginRequiredMixin, CreateView, SuccessMessage):
    model = Req
    template_name = 'add_req.html'
    form_class = ReqForm
    success_url = reverse_lazy('add_req')
    success_msg = 'Предложение добавлено'
    def get_context_data(self, **kwargs):
        kwargs['list_req'] = Req.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

class ReqsUpdateView(LoginRequiredMixin, UpdateView):
    model = Req
    template_name = 'add_req.html'
    form_class = ReqForm
    success_url = reverse_lazy('add_req')
    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs

class ReqsDeleteView(DeleteView):
    model = Req
    template_name = 'add_req.html'
    success_url = reverse_lazy('add_req')
    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user !=  self.object.author:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)

#***************************
#Deal classes

class DealListView(ListView):
    model = Deal 
    template_name = 'deals.html'
    context_object_name = 'deals'

class DealDetailView(LoginRequiredMixin, DetailView):
    model = Deal 
    template_name = 'detail_deal.html'
    context_object_name = 'get_deal'

class DealCreateView(LoginRequiredMixin, CreateView, SuccessMessage):
    model = Deal 
    template_name = 'add_deal.html'
    form_class = DealForm
    success_url = reverse_lazy('add_deal')
    success_msg = 'Сделка добавлено'
    def get_context_data(self, **kwargs):
        kwargs['list_deals'] = Deal.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

class DealUpdateView(LoginRequiredMixin, UpdateView):
    model = Deal  
    template_name = 'add_deal.html'
    form_class = Deal
    success_url = reverse_lazy('add_deal')
    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs

class DealDeleteView(DeleteView):
    model = Deal 
    template_name = 'add_deal.html'
    success_url = reverse_lazy('add_deal')
    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user !=  self.object.author:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)

#*********************
#login/registration/logout classess

class StormwindLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('home')
    def get_success_url(self):
        return self.success_url

class RegisterUserView(CreateView):
    model = User
    template_name = 'register_page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        auth_user = authenticate(username=username, password=password)
        login(self.request, auth_user)
        return form_valid

class StormwindLogoutView(LogoutView):
    next_page = reverse_lazy('home')