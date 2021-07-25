from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path('about/', views.about, name="about"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("login/", views.login, name="login"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    
    # path('', TemplateView.as_view(template_name="login.html")),

    # path('logout', LogoutView.as_view()),

    # path("handlerequest/", views.handlerequest, name="HandleRequest"),

]
