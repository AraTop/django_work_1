from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView , View, CreateView, UpdateView, DeleteView
from main.models import Blog, Product
from pytils.translit import slugify

class ProductListView(ListView):
   model = Product

class ProductsListView(ListView):
   model = Product
   template_name = 'main/products_list.html'

class ProductDetailView(DetailView):
   model = Product

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