from django.urls import path
from . import views

urlpatterns = [
    #for bank details
    path('', views.userdetails, name='userdetails'),
    path('insertbankdetails', views.insertbankdetails, name='insertbankdetails'),
    path('familydetails', views.familydetails, name='familydetails'),
    path('addfamily', views.addfamilydetails, name='addfamily'),
    path('deletefamily', views.deletefamily, name='deletefamily'),
    path('updatefamilydetails/<str:pk>', views.updatefamilydetails, name='updatefamilydetails'),
    path('deletebankdetails', views.deletebankdetails, name='deletebankdetails'),
    path('fetchbankdetails/<int:id>', views.fetchbankdetails, name='fetchbankdetails'),
    path('updatebankdetails', views.updatebankdetails, name='updatebankdetails'),
    # for credit card
    path('creditcarddetails', views.creditcarddetails, name='creditcarddetails'),
    path('insertcreditcarddetails', views.insertcreditcarddetails, name='insertcreditcarddetails'),
    path('deletecreditcard', views.deletecreditcard, name='deletecreditcard'),
    path('edit_caredit_card_details/<int:id>', views.edit_caredit_card_details, name='edit_caredit_card_details'),
    path('updatecreditcard', views.updatecreditcard, name='updatecreditcard'),
    # for other card
    path('otherloans', views.otherloans, name='otherloans'),
    path('insertotherloans', views.insertotherloans, name='insertotherloans'),
    path('deleteotherloans/<int:id>', views.deleteotherloans, name='deleteotherloans'),
    path('editotherloans/<int:id>', views.editotherloans, name='editotherloans'),
    path('updateotherloans', views.updateotherloans, name='updateotherloans'),
]






