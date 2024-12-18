from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BookViewSet, BookList


# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# create your urls here
urlpatterns = [

    # Route for the BookList view (List)
    path('books/', BookList.as_view(), name='book-list'), # Maps to the BookList view
    
    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)), # This includes all routes registers with the router

    # Implement a view that allow users obtain a token
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]