"""CryptoWheelSpin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from wheelspin.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', home, name='home'),
    path('ref/<str:ref_code>/', home, name='home'),
    path('404/', err404, name='err404'),
    path('about/', about, name='about'),
    path('affiliate/', affiliate, name='affiliate'),
    path('awards/', awards, name='awards'),
    path('bonus/', bonus, name='bonus'),
    path('cart/', cart, name='cart'),
    path('contact', contact, name='contact'),
    path('faq/', faq, name='faq'),
    path('how-it-work/', howItWork, name='how-it-work'),
    path('lottery/', lottery, name='lottery'),
    path('play/', play, name='play'),
    path('terms-conditions-details/', termsConditionsDetails, name='terms-conditions-details'),
    path('terms-conditions/', termsConditions, name='terms-conditions'),
    path('tournaments/', tournaments, name='tournaments'),
    path('game/', game, name='game'),
    path('slots/', slots, name='slots'),
    path('slotlist/<str:bet>/', slotlist, name='slotlist'),
    path('profile/', profile, name="profile"),
    path('gameresults/', gameresults, name="gameresults"),
    path('transactions/', transactions, name="transactions"),
    path('gameresults/next/<int:id>/', nextGresult, name="NextGameResult"),
    path('gameresults/pre/<int:id>/', preGresult, name="PreGameResult"),
    path('exchange/', exchange, name="exchange"),
    path('inplay/', inplay, name="inplay"),
    path('prejoin/', prejoin, name="prejoin"),
    path('leave/<str:room_name>', leave_room, name="leave_room"),
    path('games/', include('wheelspin.urls')),

]

urlpatterns += staticfiles_urlpatterns()