from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
   path("", views.ProductListView.as_view()),
   path("products/", views.ProductsListView.as_view()),####
   path("contacts/", views.ContactView.as_view()),
   path("product/<int:pk>/", views.ProductDetailView.as_view(), name='product'),
   path("blog/", views.BlogsListView.as_view(), name='blog_list'),
   path("blog/<int:pk>/", views.BlogsDetailView.as_view(), name='view'),
   path("blog/create/", views.BlogsCreateView.as_view(), name='blog_from'),
   path("blog/update/<int:pk>/", views.BlogsUpdateView.as_view()),
   path("blog/delete/<int:pk>/", views.BlogsDeleteView.as_view()),
   path("create/", views.ProductCreateView.as_view()),
   path("delete/<int:pk>/", views.ProductDeleteView.as_view()),
   path("update/<int:pk>/", views.ProductUpdateView.as_view())
]   