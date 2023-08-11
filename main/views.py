from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView, DetailView , View, CreateView, UpdateView, DeleteView
from main.forms import ProductForm, VersionForm
from main.models import Blog, Product, Version
from pytils.translit import slugify
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ContactView(View):
   template_name = 'main/contacts.html'

   def get(self, request):
      return render(request, self.template_name)

   def post(self, request):
      name = request.POST.get("name")
      phone = request.POST.get("phone")
      message = request.POST.get("message")
      print(f"name: {name}, phone: {phone}, message: {message}")
      return render(request, self.template_name)
   
#----------------------------------------------------------------------
@method_decorator(login_required, name='dispatch')
class BlogsListView(ListView):
   model = Blog

   def get_queryset(self):
      return Blog.objects.filter(is_publication=True)

@method_decorator(login_required, name='dispatch')
class BlogsDetailView(DetailView):
   model = Blog

   def get_object(self, queryset=None):
      self.object = super().get_object(queryset)
      self.object.number_of_views += 1
      self.object.save()
      return self.object

@method_decorator(login_required, name='dispatch')   
class BlogsCreateView(CreateView):
   model = Blog
   fields = ('header', 'slug', 'content', 'preview', 'date_creation', 'is_publication', 'number_of_views')
   success_url = '/blog/' 

   def form_valid(self, form):
      if form.is_valid():
         new_mat = form.save()
         new_mat.slug = slugify(new_mat.header)
         new_mat.save
         
      return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class BlogsUpdateView(UpdateView):
   model = Blog
   fields = ('header', 'slug', 'content', 'preview', 'date_creation', 'is_publication', 'number_of_views')
   success_url = '/blog/' 

   def form_valid(self, form):
      if form.is_valid():
         new_mat = form.save()
         new_mat.slug = slugify(new_mat.header)
         new_mat.save

      return super().form_valid(form)
   
   def get_success_url(self):
      return reverse('main:view', args=[self.kwargs.get('pk')])

@method_decorator(login_required, name='dispatch')
class BlogsDeleteView(DeleteView):
   model = Blog
   success_url = '/blog/' 

#----------------------------------------------------------------------
@method_decorator(login_required, name='dispatch')
class ProductCreateView(CreateView):
   model = Product 
   form_class = ProductForm
   success_url = '/' 

   def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class ProductDeleteView(DeleteView):
   model = Product
   success_url = '/' 

@method_decorator(login_required, name='dispatch')
class ProductListView(ListView):
   model = Product

   def get_queryset(self):
      return super().get_queryset().filter(user=self.request.user)
   
@method_decorator(login_required, name='dispatch')
class ProductDetailView(DetailView):
   model = Product

   def get_object(self, queryset=None):
      self.object = super().get_object(queryset)
      self.object.number_of_views += 1
      self.object.save()
      return self.object
   
   def get_queryset(self):
      return super().get_queryset().filter(user=self.request.user)
   
@method_decorator(login_required, name='dispatch')   
class ProductUpdateView(UpdateView):
   model = Product
   form_class = ProductForm
   success_url = '/'

   def get_success_url(self):
      return reverse('main:product', args=[self.kwargs.get('pk')])

   def get_context_data(self, **kwargs):
      context_data = super().get_context_data(**kwargs)
      VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)

      if self.request.method == 'POST':
         context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
      else:
         context_data['formset'] = VersionFormset(instance=self.object)

      return context_data

   def form_valid(self, form):
      formset = self.get_context_data()['formset']
      self.object = form.save()

      if formset.is_valid():
         formset.instance = self.object
         formset.save()

      return super().form_valid(form)

   def get_queryset(self):
      return super().get_queryset().filter(user=self.request.user)
   
#----------------------------------------------------------------------
@method_decorator(login_required, name='dispatch')
class ProductsListView(ListView):
   model = Product
   template_name = 'main/products_list.html'

#-------------------------------------------------------------
@method_decorator(login_required, name='dispatch')
class VersionUpdateView(UpdateView):
   model = Version 
   form_class = VersionForm
   success_url = '/' 

@method_decorator(login_required, name='dispatch')
class VersionDeleteView(DeleteView):
   model = Version
   success_url = '/' 