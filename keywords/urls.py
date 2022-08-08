from django.urls import include, path
from . import views
from .forms import Registration_form1,Registration_form2,Registration_form3
from .views import ContactWizard
urlpatterns = [
    path('', ContactWizard.as_view([Registration_form1, Registration_form2, Registration_form3])),
    path('locations', views.reglocations, name="reglocations"),
    path('locationss', views.reglocationspost, name="reglocationspost" )
]