from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView, DetailView , View, CreateView, UpdateView, DeleteView
from main.forms import ProductForm, VersionForm
from main.models import Blog, Product, Version
from pytils.translit import slugify

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

class BlogsListView(ListView):
   model = Blog

   def get_queryset(self):
      return Blog.objects.filter(is_publication=True)

class BlogsDetailView(DetailView):
   model = Blog

   def get_object(self, queryset=None):
      self.object = super().get_object(queryset)
      self.object.number_of_views += 1
      self.object.save()
      return self.object
   
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

class BlogsDeleteView(DeleteView):
   model = Blog
   success_url = '/blog/' 

#----------------------------------------------------------------------

class ProductCreateView(CreateView):
   model = Product 
   form_class = ProductForm
   success_url = '/' 

class ProductDeleteView(DeleteView):
   model = Product
   success_url = '/' 

class ProductListView(ListView):
   model = Product

class ProductDetailView(DetailView):
   model = Product

   def get_object(self, queryset=None):
      self.object = super().get_object(queryset)
      self.object.number_of_views += 1
      self.object.save()
      return self.object
   
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

#----------------------------------------------------------------------

class ProductsListView(ListView):
   model = Product
   template_name = 'main/products_list.html'

#-------------------------------------------------------------

class VersionUpdateView(UpdateView):
   model = Version 
   form_class = VersionForm
   success_url = '/' 

class VersionDeleteView(DeleteView):
   model = Version
   success_url = '/' 