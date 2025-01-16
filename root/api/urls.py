from django.urls import path
from .views import BookListCreateAPIView, BookRetrieveUpdateDeleteAPIView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDeleteAPIView.as_view(), name='book-detail'),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)