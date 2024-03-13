from django.urls import path

from .views import OrderCreateView, OrdersTemplateView, SuccessTemplateView, CancelTemplateView, OrderDetailView

app_name = 'orders'

urlpatterns = [
    path('order-create', OrderCreateView.as_view(), name='order_create'),
    path('orders', OrdersTemplateView.as_view(), name='orders'),
    path('success', SuccessTemplateView.as_view(), name='success_order'),
    path('cancel', CancelTemplateView.as_view(), name='cancel_order'),
    path('order-detail/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),

]


