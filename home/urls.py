from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("index/", views.index, name="DOMOTICA"),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("contactus/", views.contactus, name="contactus"),
    path("Products & Services/", views.services, name="services"),
    path("faq/", views.faqs, name="FAQS"),
    path("login/", views.login, name="login"),
    path("kentrance/", views.kentrance, name="Entrance Automation"),
    path("kenergy/", views.kenergy, name="Energy Management"),
    path("kkeypad/", views.kkeypad, name="Keypad Automation"),
    path("curtainmotors/", views.curtainmotors, name="Curtain Motors"),
    path("alighting/", views.alighting, name="Lighting Automation"),
    path("aaccesscontrol/", views.aaccesscontrol, name="Access Control"),
    path("aaudiovisualcontrolandacoustics/", views.aaudiovisualcontrolandacoustics, name="Audio Visual Control and Acoustics"),
    path("asecurityandsurvillence/", views.asecurityandsurvillence, name="Security and Survillance"),
    path("acentralvaccum/", views.acentralvaccum, name="Central Vaccum"),
    path("aventilationsystems/", views.aventilationsystems, name="Ventilation Systems"),
    path("terms/", views.terms, name="Terms of service"),
    path("privacy/", views.privacy, name="Privacy policy"),
    path("pricing/", views.pricing, name="Get Started"),
    path("readmore/", views.readmore, name="Read More"),

]
