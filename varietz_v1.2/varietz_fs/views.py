from django.shortcuts import render_to_response
from varietz_fs.models import *
from django.db import connection
import json,decimal
from django.template import RequestContext
from django.template.context_processors import csrf
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core import serializers
import time
from django.views.decorators.csrf import csrf_protect

def home(request):
	return HttpResponseRedirect('/base')

def Base(request):
	c = {}
	c.update(csrf(request))
	c['product_cat'] = ProductCat.objects.values('cat').distinct()
	cur = connection.cursor()
	cur.callproc('PopulateDropdown',['Electronics'])
	c['el_cat'] = cur.fetchall()
	cur.close()

	cur = connection.cursor()
	cur.callproc('PopulateDropdown',['Appliances'])
	c['apl_cat'] = cur.fetchall()
	cur.close()
	#print(c['el_cat'][1][1])
	return render_to_response('base1.html',c)

def UserBaseView(request):
	c = {}
	c.update(csrf(request))
	c['product_cat'] = ProductCat.objects.values('cat').distinct()
	cur = connection.cursor()
	cur.callproc('PopulateDropdown',['Electronics'])
	c['el_cat'] = cur.fetchall()
	cur.close()

	cur = connection.cursor()
	cur.callproc('PopulateDropdown',['Appliances'])
	c['apl_cat'] = cur.fetchall()
	cur.close()
	return render_to_response('userpage.html',c)

def electronics(request):
	c = {}
	c.update(csrf(request))
	c['product_cat'] = ProductCat.objects.values('cat').distinct()
	return render_to_response('electronics.html',c)

def contactus(request):
	c = {}
	c.update(csrf(request))
	c['product_cat'] = ProductCat.objects.values('cat').distinct()
	cur = connection.cursor()
	cur.callproc('PopulateDropdown',['Electronics'])
	c['el_cat'] = cur.fetchall()
	cur.close()

	cur = connection.cursor()
	cur.callproc('PopulateDropdown',['Appliances'])
	c['apl_cat'] = cur.fetchall()
	cur.close()
	return render_to_response('contact.html',c)

def aboutus(request):
	c = {}
	c.update(csrf(request))
	c['product_cat'] = ProductCat.objects.values('cat').distinct()
	cur = connection.cursor()
	cur.callproc('PopulateDropdown',['Electronics'])
	c['el_cat'] = cur.fetchall()
	cur.close()

	cur = connection.cursor()
	cur.callproc('PopulateDropdown',['Appliances'])
	c['apl_cat'] = cur.fetchall()
	cur.close()
	return render_to_response('aboutus.html',c)

def careers(request):
	c = {}
	c.update(csrf(request))
	c['product_cat'] = ProductCat.objects.values('cat').distinct()
	cur = connection.cursor()
	cur.callproc('PopulateDropdown',['Electronics'])
	c['el_cat'] = cur.fetchall()
	cur.close()

	cur = connection.cursor()
	cur.callproc('PopulateDropdown',['Appliances'])
	c['apl_cat'] = cur.fetchall()
	cur.close()
	return render_to_response('careers.html',c)

def terms12(request):
	c = {}
	c.update(csrf(request))
	c['product_cat'] = ProductCat.objects.values('cat').distinct()
	cur = connection.cursor()
	cur.callproc('PopulateDropdown',['Electronics'])
	c['el_cat'] = cur.fetchall()
	cur.close()

	cur = connection.cursor()
	cur.callproc('PopulateDropdown',['Appliances'])
	c['apl_cat'] = cur.fetchall()
	cur.close()
	return render_to_response('Terms.html',c)


def login(request):
	c = {}
	c.update(csrf(request))
	c['product_cat'] = ProductCat.objects.values('cat').distinct()
	cur = connection.cursor()
	cur.callproc('PopulateDropdown',['Electronics'])
	c['el_cat'] = cur.fetchall()
	cur.close()

	cur = connection.cursor()
	cur.callproc('PopulateDropdown',['Appliances'])
	c['apl_cat'] = cur.fetchall()
	cur.close()
	return render_to_response('register.html',c)

def RenderNewPage(request):
	c = {}
	#c.update(csrf(request))
	c['href'] = '/base/userpage.html'
	c['TopLI'] = request.POST['TopLI']
	c['MidleLI'] = request.POST['MidleLI']
	c['PCat'] = request.POST['PCat']

	return HttpResponse(json.dumps(c, default=decimal_default), content_type = "application/json")
	#return render_to_response('userpage.html',c)

def LoadFashionPage(request):
	PCat = request.POST['PCat']
	cur = connection.cursor()
	cur.callproc('get_bs_results',[PCat])  
	results = cur.fetchall()
	cur.close()
	jsonresponse = {
	'TrendFP': results
	}
	#print(jsonresponse)
	return HttpResponse(json.dumps(jsonresponse, default=decimal_default), content_type = "application/json")

def LoadElectronicsPage(request):
	PCat = request.POST['PCat']
	cur = connection.cursor()
	cur.callproc('LoadElectronicsResult',[PCat])  
	results = cur.fetchall()
	cur.close()
	jsonresponse = {
	'TrendEP': results
	}
	#print(jsonresponse)
	return HttpResponse(json.dumps(jsonresponse, default=decimal_default), content_type = "application/json")

def LoadAppliancesPage(request):
	PCat = request.POST['PCat']
	cur = connection.cursor()
	cur.callproc('LoadAPLResult',[PCat])  
	results = cur.fetchall()
	cur.close()
	jsonresponse = {
	'TrendAP': results
	}
	#print(jsonresponse)
	return HttpResponse(json.dumps(jsonresponse, default=decimal_default), content_type = "application/json")


def getImgPriceHis(request):
	StyleID = request.POST['StyleID']
	cur = connection.cursor()
	#cur.callproc('get_price_history',[Comps,StyleID]) 
	cur.callproc('get_price_history',[StyleID]) 
	results = cur.fetchall()
	cur.close()
	jsonresponse = {
	'LABM': results
	}
	return HttpResponse(json.dumps(jsonresponse, default=decimal_default), content_type = "application/json")

def decimal_default(obj):
	if isinstance(obj,decimal.Decimal):
		return float(obj)
	elif hasattr(obj,'isoformat'):
		return obj.isoformat()
	else:
		raise TypeError	