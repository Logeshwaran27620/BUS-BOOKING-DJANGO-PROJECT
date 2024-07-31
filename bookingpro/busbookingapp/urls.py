
from django.urls import  path
from busbookingapp import views


urlpatterns =[
    path('2/',views.user_login),
    path('1/',views.main),
    path('fi/',views.first),
    path('',views.regist),
    path("book/",views.orderlist),
    path("contact/",views.contact),
    path("gallery/",views.gallery),
    path("chncbe/",views.chn_cbe),
    path('bookingg/', views.bookingg, name='booking'),  # The booking view
    path('chnmdu/', views.mdu_chn, name='madurai_to_CHENNAI_page'),
    path("seat/",views.seatselection),
    path("chnmdu/",views.busdb),
    path("mduchn/",views.busdb1),
    path("chndpm/",views.busdb2),
    path("dpmchn/",views.busdb3),
    path("form/",views.bookdetail),
    path("payment/",views.paymentdetail),
    path("mk/",views.makepayment),
    path('catfilter/<int:a>',views.cat_filter),



    
]


