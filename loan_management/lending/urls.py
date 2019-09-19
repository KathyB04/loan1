from django.conf.urls import url

from .views import index, new_borrower, delete_borrower, update_customer_info, view_customer_info

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^new_borrower$', new_borrower, name ='new_borrower'),
	url(r'^delete_borrower/(?P<borrower_id>\d+)$', delete_borrower, name = 'delete_borrower'),
	url(r'^update_customer_info/(?P<borrower_id>\d+)$', update_customer_info, name = 'update_customer_info'),
	url(r'^view_customer_info/(?P<borrower_id>\d+)$', view_customer_info, name = 'view_customer_info'),
	]